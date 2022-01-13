# Copyright (C) 2022, Giorgio Comitini
#
# This is part of the PySmeQcd Documentation.
#
# See the file index.rst for copying conditions.
#
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#import pathlib
#import os, sys
#sys.path.insert(0, os.path.abspath('../../src'))
import PySmeQcd


# -- Project information -----------------------------------------------------

project = 'PySmeQcd'
copyright = '2022, Giorgio Comitini'
author = 'Giorgio Comitini'

# The full version, including alpha/beta/rc tags
release = '1.1.0-alpha'
version = '1.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx_copybutton',
    'sphinx.ext.autosummary',
    'sphinx.ext.imgmath',
]

add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

html_theme_options = {
    'github_user': 'GComitini',
    'github_repo': 'PySmeQcd',
    'description': 'A Python library for the Screened Massive Expansion of QCD',
    'sidebar_width': '24%',
    'sidebar_includehidden': 'false',
    'show_relbar_bottom': 'true',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

modindex_common_prefix = ['PySmeQcd.', 'PySmeQcd.oneloop.']

# html_logo = ""
# html_favicon = ""

imgmath_latex_preamble = r'\usepackage{slashed}'
imgmath_image_format = 'svg'
imgmath_dvisvgm_args = ['--no-fonts', '-c', '1.2']

latex_show_urls = 'footnote'
latex_show_pagerefs = True

latex_elements = {
    'preamble': r'\usepackage{slashed}',
}
