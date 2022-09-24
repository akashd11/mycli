import click
from click import formatting
from click.types import CompositeParamType
from click_default_group import DefaultGroup
from toolkit import __version__
import comp


@click.group(cls=DefaultGroup, default="serve", default_if_no_args=True)
@click.version_option(version=__version__)
def cli():
    """jdhfgjdhf
    """


@cli.command()
@click.argument("files", type=click.Path(exists=True), nargs=-1)
def create(name: str):
    comp.create(name)



