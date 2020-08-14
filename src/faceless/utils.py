def add_path_suffix(path: str, suffix: str = "_faceless"):
    """

    Args:
        path:
        suffix:

    Returns:

    """
    path_parts = path.split(".")
    path = "".join(path_parts[:-1]) + suffix + "." + path_parts[-1]
    return path
