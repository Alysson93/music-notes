from pytest import mark, raises

from music_notes.scales import scale


def test_fucniona_com_tonica_minuscula():
    result = scale('c', 'maior')
    assert result == {
        'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }


def test_erro_tonica_inexistente():
    msg = 'Esta nota não existe.'
    with raises(ValueError) as error:
        scale('x', 'maior')
    assert msg == error.value.args[0]


def test_erro_escala_inexistente():
    msg = 'Esta escala não existe ou ainda não foi implementada.'
    with raises(KeyError) as error:
        scale('D', 'meior')
    assert msg == error.value.args[0]


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('D', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('F', ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']),
        ('Cb', ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb']),
    ],
)
def test_retorna_escalas_corretas(tonica, esperado):
    result = scale(tonica, 'maior')
    assert result['notes'] == esperado


def test_retorna_graus_corretos():
    result = scale('C', 'maior')
    assert result['degrees'] == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
