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

SCALES = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def get_index(tonica: str):
    for i in NOTES:
        if tonica in i:
            return NOTES.index(i)


def get_seq(tonica: str):
    SEQ = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    seq = SEQ[SEQ.index(tonica[0]) :]
    seq += SEQ[: SEQ.index(tonica[0])]
    return seq
