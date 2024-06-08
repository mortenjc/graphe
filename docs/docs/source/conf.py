# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'graphe'
copyright = '2023 - 2024, Morten Jagd Christensen'
author = 'Morten Jagd Christensen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # was 'nature'
html_logo = "_static/graphe_logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    "home_page_in_toc": True,
    "show_navbar_depth": 1
}
html_static_path = ['_static']
html_css_files = ["custom.css"]
