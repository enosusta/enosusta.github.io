"""Shared Sphinx configuration for every language."""

import os
from pathlib import Path


DOCS_DIR = Path(__file__).resolve().parent
SITE_URL = "https://enosusta.github.io"
SUPPORTED_LANGUAGES = {"en", "ja"}
GOOGLE_SITE_VERIFICATION = os.environ.get("GOOGLE_SITE_VERIFICATION", "").strip()
SEARCH_EXCLUDED_PAGES = {
    "404",
    "genindex",
    "search",
    *(f"notes/griffithsqm/chap2/2-{number}" for number in range(58, 65)),
}

language = os.environ.get("DOCS_LANGUAGE", "ja")
if language not in SUPPORTED_LANGUAGES:
    supported = ", ".join(sorted(SUPPORTED_LANGUAGES))
    raise RuntimeError(
        f"Unsupported DOCS_LANGUAGE={language!r}; expected one of: {supported}"
    )

# -- Project information -----------------------------------------------------

project = "Enos's Archive"
copyright = "2026, Enos"
author = "Enos"
release = "1.0.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "matplotlib.sphinxext.plot_directive",
    "notfound.extension",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_exec_code",
    "sphinx_sitemap",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
    "sphinx_last_updated_by_git",
]

root_doc = "index"
templates_path = [str(DOCS_DIR / "_templates")]
exclude_patterns = []

bibtex_bibfiles = [str(DOCS_DIR / "references.bib")]
suppress_warnings = ["bibtex.duplicate_citation"]
autosectionlabel_prefix_document = True
todo_include_todos = True
todo_link_only = True

# -- HTML output -------------------------------------------------------------

html_title = project
html_theme = "sphinx_rtd_theme"
html_static_path = [str(DOCS_DIR / "_static")]
html_css_files = ["custom.css"]
html_favicon = str(DOCS_DIR / "_static" / "logo.svg")
html_baseurl = f"{SITE_URL}/{language}/"

language_labels = {"en": "EN", "ja": "JA"}
language_documents = {
    code: sorted(
        path.relative_to(DOCS_DIR / "source" / code).with_suffix("").as_posix()
        for path in (DOCS_DIR / "source" / code).rglob("*.rst")
    )
    for code in SUPPORTED_LANGUAGES
}
available_languages = sorted(
    (code for code, documents in language_documents.items() if "index" in documents),
    key=lambda code: (code != "ja", code),
)
all_documents = {
    pagename
    for documents in language_documents.values()
    for pagename in documents
}
alternate_language_links = {}
for pagename in sorted(all_documents - SEARCH_EXCLUDED_PAGES):
    links = [
        {
            "code": code,
            "url": f"{SITE_URL}/{code}/{pagename}.html",
        }
        for code in available_languages
        if pagename in language_documents[code]
    ]
    if len(links) > 1:
        alternate_language_links[pagename] = links

html_theme_options = {
    "analytics_anonymize_ip": False,
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "vcs_pageview_mode": "blob",
    "style_nav_header_background": "#2980b9",
    "flyout_display": "hidden",
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

html_context = {
    "display_github": True,
    "github_user": "enosusta",
    "github_repo": "enosusta.github.io",
    "github_version": "main",
    "conf_py_path": f"/docs/source/{language}/",
    "current_language": language,
    "search_excluded_pages": sorted(SEARCH_EXCLUDED_PAGES),
    "alternate_language_links": alternate_language_links,
    "x_default_url": f"{SITE_URL}/",
    "google_site_verification": GOOGLE_SITE_VERIFICATION,
    "language_links": [
        {
            "code": code,
            "label": language_labels[code],
            "url": f"/{code}/",
            "documents": language_documents[code],
        }
        for code in available_languages
    ],
}

notfound_urls_prefix = f"/{language}/"
sitemap_url_scheme = "{link}"
sitemap_excludes = [
    f"{pagename}.html" for pagename in sorted(SEARCH_EXCLUDED_PAGES)
]

ogp_site_url = html_baseurl
ogp_social_cards = {"enable": False}

# -- MathJax -----------------------------------------------------------------

default_role = "math"
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
