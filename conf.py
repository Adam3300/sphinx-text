# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os, sys

project = 'VVP'
copyright = '2024, Ververica'
author = 'VERA'
release = '3.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


sys.path.insert(0, os.path.abspath('./ext'))

extensions = ['toctree_filter']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

#html_theme_options = {
#"navbar_start": ["navbar-logo"],
#"navbar_center": [],
#"navbar_end": ["navbar-icon-links"]
#}

html_theme_options = {
   "navbar_center": [],
   "secondary_sidebar_items": ["page-toc"],
}

html_scaled_image_link = False

html_css_files = [
    'css/custom.css',
]

html_static_path = ['_static']

html_context = {
   "default_mode": "dark",
}
