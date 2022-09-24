import click
import sys
from click_default_group import DefaultGroup
from version import __version__
import comp


@click.group(cls=DefaultGroup, default="create", default_if_no_args=True)
@click.version_option(version=__version__)
def cli():
    """jdhfgjdhf
    """


@cli.command()
@click.argument("name", type=click.Path(exists=True), nargs=-1)
def create(name: str):
    comp.create(name)



