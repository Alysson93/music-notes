from music_notes.chords import chord
from music_notes.scales import scale


def _triade_na_escala(nota, notas_escala) -> str:
    """
    Verifica se as notas de um acorde estão na escala.

    Examples:
        >>> _triade_na_escala('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'

        >>> _triade_na_escala('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
    """
    tonica, terca, quinta = chord(nota)['notes']
    match terca in notas_escala, quinta in notas_escala:
        case True, True:
            return tonica
        case False, True:
            return f'{tonica}m'
        case False, False:
            return f'{tonica}°'


def _convert_degree(cifra, degree):
    """
    Converte o grau relativo à cifra

    Examples:
        >>> _convert_degree('C', 'I')
        'I'

        >>> _convert_degree('Cm', 'I')
        'i'

        >>> _convert_degree('C°', 'I')
        'i-'
    """
    if 'm' in cifra:
        return degree.lower()
    elif '°' in cifra:
        return degree.lower() + '-'
    else:
        return degree


def harmonic_field(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera um campo harmônico a partir de uma tônica e uma tonalidade.

    Args:
        tonica: Nota que será a tônica do campo harmônico.
        tonalidade: Tonalidade da escala. (maior, menor)

    Returns:
        Um dicionário com os acordes e graus do campo harmônico.

    Raises:
        ValueError: Caso a tõnica não seja uma nota válida.
        KeyError: Caso a tonalidade não exista ou não tenha sido implementada.

    Examples:
        >>> harmonic_field('C', 'maior')
        {'chords': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'], 'degrees': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii-']}
    """
    notes, _deg = scale(tonica, tonalidade).values()
    chords = [_triade_na_escala(note, notes) for note in notes]
    degrees = [
        _convert_degree(chord, degree) for chord, degree in zip(chords, _deg)
    ]
    return {'chords': chords, 'degrees': degrees}
