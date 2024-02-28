from music_notes.scales import scale


def chord(cifra: str) -> dict[str, list[str]]:
    """
    Gera um acorde a partir de uma cifra.

    Args:
        cifra: Nome do acorde.

    Returns:
        Um dicionário com as notas e graus do acorde.

    Raises:
        ValueError: Caso a cifra não seja válida.

    Examples:
        >>> chord('C')
        {'notes': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}

        >>> chord('Cm')
        {'notes': ['C', 'Eb', 'G'], 'degrees': ['I', 'III-', 'V']}

        >>> chord('C°')
        {'notes': ['C', 'Eb', 'Gb'], 'degrees': ['I', 'III-', 'V-']}

        >>> chord('C+')
        {'notes': ['C', 'E', 'G#'], 'degrees': ['I', 'III', 'V+']}

        >>> chord('Cm+')
        {'notes': ['C', 'Eb', 'G#'], 'degrees': ['I', 'III-', 'V+']}
    """
    indexes = (0, 2, 4)
    if cifra.endswith('m+'):
        cifra = cifra[:-2]
        degrees = ['I', 'III-', 'V+']
        tonalidade = 'menor-quinta-aumentada'
    elif cifra.endswith('m'):
        cifra = cifra[:-1]
        degrees = ['I', 'III-', 'V']
        tonalidade = 'eolio'
    elif cifra.endswith('°'):
        cifra = cifra[:-1]
        degrees = ['I', 'III-', 'V-']
        tonalidade = 'locrio'
    elif cifra.endswith('+'):
        cifra = cifra[:-1]
        degrees = ['I', 'III', 'V+']
        tonalidade = 'quinta-aumentada'
    else:
        degrees = ['I', 'III', 'V']
        tonalidade = 'jonio'
    try:
        notes = scale(cifra, tonalidade)['notes']
    except ValueError:
        raise ValueError('Esta cifra não existe.')
    notes = [notes[index] for index in indexes]
    return {'notes': notes, 'degrees': degrees}
