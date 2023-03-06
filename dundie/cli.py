import pkg_resources
import rich_click as click
from rich.table import Table
from rich.console import Console

from dundie import core


click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """(Entry point)Dunder Mifflin rewards system \n.

    This cli application controls DM rewards.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database

    ## Features
    - validades data
    - parses the file
    - loads to data base
    """
    table = Table(title="Dunder Mifflin Associates")
    headers = ["name", "dept", "role", "e-mail"]
    result = core.load(filepath)

    for header in headers:
        table.add_column(header, style="magenta")

    for person in result:
        table.add_row(*[field.strip() for field in person.split(",")])

    console = Console()
    console.print(table)
