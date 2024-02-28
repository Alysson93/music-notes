from pytest import mark
from typer.testing import CliRunner

from music_notes.cli import app

runner = CliRunner()


def test_escala_cli_retorna_0_stdout():
    result = runner.invoke(
        app,
        [
            'scales',
        ],
    )
    assert result.exit_code == 0


@mark.parametrize('note', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'])
def test_escala_cli_deve_conter_notas(note):
    result = runner.invoke(
        app,
        [
            'scales',
        ],
    )
    assert note in result.stdout


@mark.parametrize('note', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_deve_conter_graus(note):
    result = runner.invoke(
        app,
        [
            'scales',
        ],
    )
    assert note in result.stdout


def test_acorde_cli_retorna_0_stdout():
    result = runner.invoke(
        app,
        [
            'chords',
        ],
    )
    assert result.exit_code == 0


@mark.parametrize('note', ['A', 'C#', 'E'])
def test_escala_cli_deve_conter_notas(note):
    result = runner.invoke(
        app,
        [
            'chords',
        ],
    )
    assert note in result.stdout


@mark.parametrize('note', ['I', 'III', 'V'])
def test_acorde_cli_deve_conter_graus(note):
    result = runner.invoke(
        app,
        [
            'chords',
        ],
    )
    assert note in result.stdout


def test_campo_harmonico_cli_retorna_0_stdout():
    result = runner.invoke(
        app,
        [
            'harmonic-fields',
        ],
    )
    assert result.exit_code == 0


@mark.parametrize('note', ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#°'])
def test_campo_harmonico_cli_deve_conter_notas(note):
    result = runner.invoke(
        app,
        [
            'harmonic-fields',
        ],
    )
    assert note in result.stdout


@mark.parametrize('note', ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii-'])
def test_campo_harmonico_cli_deve_conter_graus(note):
    result = runner.invoke(
        app,
        [
            'harmonic-fields',
        ],
    )
    assert note in result.stdout
