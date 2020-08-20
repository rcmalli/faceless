"""Command-line interface."""
import click
from click import Context

from faceless.utils import add_path_suffix


@click.group()
@click.option("--input", help="The Path of input image/video file.")
@click.option("--debug/--no-debug", default=False)
@click.version_option()
@click.pass_context
def main(ctx: click.Context, input: str, debug: bool) -> None:
    """Faceless.

    Main function to run all processes.

    Args:
        ctx (click.Context): The context manager for the click.
        input (str): Input path for the files.
        debug (bool): Switch for activating the debug mode.
    """
    ctx.obj = {} if ctx.obj is None else ctx.obj
    ctx.obj["input"] = input
    ctx.obj["output"] = add_path_suffix(ctx.obj["input"])
    click.echo("Debug mode is %s" % ("on" if debug else "off"))


@main.command()
@click.pass_context
def blur(ctx: click.Context) -> None:
    """Blur Functionality.

    Args:
        ctx (click.Context): The context manager for the click.
    """
    click.echo("Blurring")


@main.command()
@click.pass_context
def cloak(ctx: click.Context) -> None:
    """Cloak Functionality.

    Args:
        ctx (click.Context): The context manager for the click.
    """
    click.echo("Cloaking")


@main.command()
@click.pass_context
def pixelate(ctx: click.Context) -> None:
    """Pixelation Functionality.

    Args:
        ctx (click.Context): The context manager for the click.
    """
    click.echo("Pixelating")


if __name__ == "__main__":
    main(obj={}, prog_name="faceless")
