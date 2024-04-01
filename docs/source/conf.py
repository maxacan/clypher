import os
import sys

sys.path.insert(0, os.path.abspath('../../src/clypher'))

from _version import __version__

project = 'Clypher'
copyright = '2024, Maximiliano Cancelarich'
author = 'Maximiliano Cancelarich'
release = __version__
version = __version__

extensions = [
    "sphinx.ext.autodoc"
]

autodoc_default_options = {
    "members": True
}

autodoc_member_order = "bysource"

autodoc_typehints = "description"

templates_path = ['_templates']
exclude_patterns = []


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
