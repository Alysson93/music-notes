NOTES = (
    ('B#', 'C', 'Dbb'),
    ('B##', 'C#', 'Db'),
    ('C##', 'D', 'Ebb'),
    ('C###', 'D#', 'Eb'),
    ('D##', 'E', 'Fb'),
    ('E#', 'F', 'Gbb'),
    ('E##', 'F#', 'Gb'),
    ('F##', 'G', 'Abb'),
    ('F###', 'G#', 'Ab'),
    ('G##', 'A', 'Bbb'),
    ('G###', 'A#', 'Bb'),
    ('A##', 'B', 'Cb'),
)

SCALES = {
    'maior': (0, 2, 4, 5, 7, 9, 11),
    'menor': (0, 2, 3, 5, 7, 8, 10),
    'jonio': (0, 2, 4, 5, 7, 9, 11),
    'dorio': (0, 2, 3, 5, 7, 9, 10),
    'frigio': (0, 1, 3, 5, 7, 8, 10),
    'lidio': (0, 2, 4, 6, 7, 9, 11),
    'mixolidio': (0, 2, 4, 5, 7, 9, 10),
    'eolio': (0, 2, 3, 5, 7, 8, 10),
    'locrio': (0, 1, 3, 5, 6, 8, 10),
    'quinta-aumentada': (0, 2, 4, 5, 8, 9, 11),
    'menor-quinta-aumentada': (0, 2, 3, 5, 8, 9, 11),
}


def get_index(tonica: str):
    for i in NOTES:
        if tonica in i:
            return NOTES.index(i)


def get_seq(tonica: str):
    SEQ = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    seq = SEQ[SEQ.index(tonica[0]) :] + SEQ[: SEQ.index(tonica[0])]
    return seq
