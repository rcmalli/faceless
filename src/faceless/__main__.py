"""Command-line interface."""
import click

from .utils import add_path_suffix


@click.group()
@click.option("--input", help="The Path of input image/video file.")
@click.version_option()
@click.pass_context
def main(ctx: click.Context, input: str) -> None:
    """Faceless.

    Main function to run all processes.

    Args:
        ctx (click.Context): The context manager for the click.
        input (str): Input path for the files.
    """
    ctx.obj["input"] = input
    ctx.obj["output"] = add_path_suffix(ctx.obj["input"])
    print(ctx)


@main.command()
@click.pass_context
def blur(ctx: click.Context) -> None:
    """Blur Functionality.

    Args:
        ctx (click.Context): The context manager for the click.
    """
    print("Blurring")


@main.command()
@click.pass_context
def cloak(ctx: click.Context) -> None:
    """Cloak Functionality.

    Args:
        ctx (click.Context): The context manager for the click.
    """
    print("Cloaking")


@main.command()
@click.pass_context
def pixelate(ctx: click.Context) -> None:
    """Pixelation Functionality.

    Args:
        ctx (click.Context): The context manager for the click.
    """
    print("Pixelating")


if __name__ == "__main__":
    main(obj={}, prog_name="faceless")  # pragma: no cover
