"""Command-line interface."""
import click

from .utils import add_path_suffix


@click.group()
@click.option("--input", help="The Path of input image/video file.")
@click.option(
    "--output",
    help="The Path of output file name. The default value is the same file "
    "as input image/video file with a suffix",
)
@click.version_option()
@click.pass_context
def main(ctx, input: str, output: str = None) -> None:
    """Faceless.

    Main function to run all processes.

    Args:
        ctx (object): The context manager for the click.
        input (str): Input path for the files.
        output (str): The output file for the processed file.
    """
    ctx.obj["input"] = input
    ctx.obj["output"] = add_path_suffix(ctx.obj["input"]) if output is None else output

    print(ctx)


@main.command()
@click.pass_context
def blur(ctx):
    """Blur Functionality.

    Args:
        ctx (object): The context manager for the click.
    """
    print("Blurring")


@main.command()
@click.pass_context
def cloak(ctx):
    """Cloak Functionality.

    Args:
        ctx (object): The context manager for the click.
    """
    print("Cloaking")


@main.command()
@click.pass_context
def pixelate(ctx):
    """Pixelation Functionality.

    Args:
        ctx (object): The context manager for the click.
    """
    print("Pixelating")


if __name__ == "__main__":
    main(obj={}, prog_name="faceless")  # pragma: no cover
