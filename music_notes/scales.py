from music_notes.utils import NOTES, SCALES, get_index, get_seq


def scale(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Args:
        tonica: Nota que será a tônica da escala.
        tonalidade: Tonalidade da escala. (maior, menor, etc)

    Returns:
        Um dicionário com as notas e graus da escala.

    Raises:
        ValueError: Caso a tõnica não seja uma nota válida.
        KeyError: Caso a tonalidade não exista ou não tenha sido implementada.

    Examples:
        >>> scale('C', 'maior')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('Bb', 'maior')
        {'notes': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('C#', 'maior')
        {'notes': ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.capitalize()
    try:
        intervals = SCALES[tonalidade.lower()]
        tonica_pos = get_index(tonica)
        seq = get_seq(tonica)
    except ValueError:
        raise ValueError('Esta nota não existe.')
    except KeyError:
        raise KeyError('Esta escala não existe ou ainda não foi implementada.')
    result = []
    cont = 0
    for interval in intervals:
        note = (tonica_pos + interval) % 12
        if NOTES[note][0].startswith(seq[cont]):
            version = 0
        elif NOTES[note][1].startswith(seq[cont]):
            version = 1
        else:
            version = 2
        result.append(NOTES[note][version])
        cont += 1
    return {
        'notes': result,
        'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
