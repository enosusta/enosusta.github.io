# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Enos\'s Archive'
copyright = '2026, Enos'
author = 'Enos'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.bibtex",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_exec_code",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "notfound.extension",
]

bibtex_bibfiles = ['references.bib']
autosectionlabel_prefix_document = True
todo_include_todos = True
todo_link_only = True

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'Enos\'s Archive'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/logo.svg'
html_baseurl = 'https://enosusta.github.io/'
html_theme_options = {
    # 'analytics_id': 'G-XXXXXXXXXX',
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': 'blob',
    'style_nav_header_background': '#2980b9',
    'flyout_display': 'hidden',
    'version_selector': True,
    'language_selector': True,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
html_context = {
    'display_github': True,
    'github_user': 'enosusta',
    'github_repo': 'enosusta.github.io',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}

notfound_urls_prefix = '/'

ogp_site_url = 'https://enosusta.github.io/'
ogp_social_cards = {
    "font": "Noto Sans CJK JP",
    "enable": False,
}

# -- Options for LaTeX output ------------------------------------------------

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
            "eqqcolon": r"=\mathrel{\mathop:}",
            "dd": r"\mathrm{d}",
            "up": r"\uparrow",
            "down": r"\downarrow",
            "bm": [r"\boldsymbol{#1}", 1],
            "dv": [r"\frac{\mathrm{d} #1}{\mathrm{d} #2}", 2],
            "pdv": [r"\frac{\partial #1}{\partial #2}", 2],
            "ket": [r"\left| #1 \right\rangle", 1],
            "bra": [r"\left\langle #1 \right|", 1],
            "braket": [r"\left\langle #1 \right\rangle", 1],
        }
    }
}
