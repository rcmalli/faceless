"""Command-line interface."""
import click

from faceless.utils import add_path_suffix


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

    Args:
        ctx:
        input:
        output:
    """
    ctx.obj["input"] = input
    ctx.obj["output"] = add_path_suffix(ctx.obj["input"]) if output is None else output

    print(ctx)


@main.command()
@click.pass_context
def blur(ctx):
    """

    Args:
        ctx:
    """
    print("Blurring")


@main.command()
@click.pass_context
def cloak(ctx):
    """

    Args:
        ctx:
    """
    print("Cloaking")


@main.command()
@click.pass_context
def pixelate(ctx):
    """

    Args:
        ctx:
    """
    print("Pixelating")


if __name__ == "__main__":
    main(obj={}, prog_name="faceless")  # pragma: no cover
