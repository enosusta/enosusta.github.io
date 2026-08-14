# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Seminarium'
copyright = '2026, Enos'
author = 'Enos'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.bibtex",
]

bibtex_bibfiles = ['references.bib']

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'Seminarium'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

default_role = 'math'
mathjax3_config = {
    "tex": {
        "macros": {
            "R": r"\mathbb{R}",
            "C": r"\mathbb{C}",
            "N": r"\mathbb{N}",
            "Z": r"\mathbb{Z}",
            "Q": r"\mathbb{Q}",
            "coloneqq": r"\mathrel{\mathop:}=",
            "dd": r"\mathrm{d}",
            "bm": [r"\boldsymbol{#1}", 1],
            "dv": [r"\frac{\mathrm{d} #1}{\mathrm{d} #2}", 2],
            "pdv": [r"\frac{\partial #1}{\partial #2}", 2],
            "ket": [r"\left| #1 \right\rangle", 1],
            "bra": [r"\left\langle #1 \right|", 1],
            "braket": [r"\left\langle #1 \right\rangle", 1],
        }
    }
}
