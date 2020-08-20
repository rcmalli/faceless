"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

from faceless import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0


def test_blur(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.blur)
    assert result.exit_code == 0


def test_pixelate(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.pixelate)
    assert result.exit_code == 0


def test_cloak(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.cloak)
    assert result.exit_code == 0
