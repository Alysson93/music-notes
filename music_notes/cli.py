from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from music_notes.chords import chord
from music_notes.harmonic_fields import harmonic_field
from music_notes.scales import scale

app = Typer()
console = Console()


@app.command()
def scales(
    tonica: str = Argument('A', help='Tônica da escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da escala'),
):
    table = Table()
    notes, degrees = scale(tonica, tonalidade).values()
    for degree in degrees:
        table.add_column(degree)
    table.add_row(*notes)
    console.print(table)


@app.command()
def chords(cifra: str = Argument('A', help='Cifra')):
    table = Table()
    notes, degrees = chord(cifra).values()
    for degree in degrees:
        table.add_column(degree)
    table.add_row(*notes)
    console.print(table)


@app.command()
def harmonic_fields(
    tonica: str = Argument('A', help='Tônica do campo harmônico'),
    tonalidade: str = Argument('maior', help='Tonalidade do campo harmônico'),
):
    table = Table()
    chords, degrees = harmonic_field(tonica, tonalidade).values()
    for degree in degrees:
        table.add_column(degree)
    table.add_row(*chords)
    console.print(table)
