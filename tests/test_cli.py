from pytest import mark
from typer.testing import CliRunner

from music_notes.cli import app

runner = CliRunner()


def test_escala_cli_retorna_0_stdout():
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('note', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_deve_conter_notas(note):
    result = runner.invoke(app)
    assert note in result.stdout


@mark.parametrize('note', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_deve_conter_graus(note):
    result = runner.invoke(app)
    assert note in result.stdout
