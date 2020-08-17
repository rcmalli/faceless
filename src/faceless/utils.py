"""Utility Functions."""


def add_path_suffix(path: str, suffix: str = "_faceless") -> str:
    """Adds suffix word to path given.

    Args:
        path (str): The path string to be formatted.
        suffix (str): The suffix word to be added after given path.

    Returns:
        Edited path.
    """
    path_parts = path.split(".")
    path = "".join(path_parts[:-1]) + suffix + "." + path_parts[-1]
    return path
