from pytest import mark, raises

from music_notes.chords import chord


def test_erro_cifra_inexistente():
    msg = 'Esta cifra não existe.'
    with raises(ValueError) as error:
        chord('x')
    assert msg == error.value.args[0]


@mark.parametrize(
    'cifra, esperado',
    [
        ('D', ['D', 'F#', 'A']),
        ('Dm', ['D', 'F', 'A']),
        ('D°', ['D', 'F', 'Ab']),
        ('Dm+', ['D', 'F', 'A#']),
        ('D+', ['D', 'F#', 'A#']),
    ],
)
def test_retorna_notas(cifra, esperado):
    notes, _ = chord(cifra).values()
    assert notes == esperado


@mark.parametrize(
    'cifra, esperado', [('D', ['I', 'III', 'V']), ('Dm', ['I', 'III-', 'V'])]
)
def test_retorna_graus(cifra, esperado):
    _, degrees = chord(cifra).values()
    assert degrees == esperado
