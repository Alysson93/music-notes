from pytest import mark, raises

from music_notes.harmonic_fields import harmonic_field


def test_fucniona_com_tonica_minuscula():
    result = harmonic_field('c', 'maior')
    assert result == {
        'chords': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'],
        'degrees': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii-'],
    }


def test_erro_tonica_inexistente():
    msg = 'Esta nota não existe.'
    with raises(ValueError) as error:
        harmonic_field('x', 'maior')
    assert msg == error.value.args[0]
