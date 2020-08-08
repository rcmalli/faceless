"""Sphinx configuration."""
from datetime import datetime


project = "Faceless"
author = "Refik Can MALLI"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
autodoc_typehints = "description"
