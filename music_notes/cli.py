from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

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
