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
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os

from sphinx.highlighting import lexers
from pygments.lexers.data import YamlLexer

# -- Project information -----------------------------------------------------

project = 'Common Workflow Language User Guide'
copyright = '2013, CWL Project Team'
author = 'CWL Project Team'

# The full version, including alpha/beta/rc tags
release = '0.1'

# Define the version we use for matching in the version switcher.
version_match = os.environ.get("READTHEDOCS_VERSION")
json_url = "https://common-workflow-languageuser-guide.readthedocs.io/en/latest/_static/switcher.json"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
]

# myst-parser settings
myst_heading_anchors = 3
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'substitution',
    'replacements',
]
myst_substitutions = {
    'repo_url': 'https://github.com/common-workflow-language/user_guide/',
    'source_branch': 'main',
}

master_doc = 'index'

pygments_style = 'sphinx'

# Set the default role so we can use `foo` instead of ``foo``
default_role = 'literal'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# CONTRIBUTING.md is referenced in the footer, but not linked via Sphinx
# aio.md is also referenced in one page, but not directly via Sphinx, hence the exclusions here.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'venv',
    'bin',
    'README.md',
    '.git',
    '.idea',
    'CONTRIBUTING.md',
    'aio.md',
    '_includes/aio-script.md'
]

source_suffix = ['.rst', '.md']

# -- Options for Pygments ----------------------------------------------------

# TODO: maybe write our own lexer to customize tokens, keywords, etc?
lexers['cwl'] = YamlLexer()

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/images/logos/cwl/CWL-Logo-HD-cropped2.png'
html_favicon = '_static/images/favicons/cwl/favicon.ico'

html_sidebars = {
    # TODO: this removes the sidebar with links from the episodes pages, but also
    #       removes the Episodes from the navigation-center template?
    # "_episodes/*": [],
    "**": ["search-field.html", "sidebar-nav-bs.html"]
}

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/common-workflow-language/user_guide/",
            "icon": "fab fa-github-square",
        },
    ],
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    "use_edit_page_button": True,
    "navbar_align": "content",
    "navbar_end": ["version-switcher", "navbar-icon-links"],
    "show_nav_level": 2,
    "navigation_depth": 2,
    "collapse_navigation": True,
    "show_prev_next": True,
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "images/favicons/cwl/favicon-16x16.png"
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "images/favicons/cwl/favicon-32x32.png"
        },
        {
            "rel": "icon",
            "sizes": "96x96",
            "href": "images/favicons/cwl/favicon-96x96.png"
        },
        {
            "rel": "icon",
            "sizes": "128x128",
            "href": "images/favicons/cwl/favicon-128.png"
        },
        {
            "rel": "icon",
            "sizes": "196x196",
            "href": "images/favicons/cwl/favicon-196x196.png"
        }
    ],
    "footer_items": ["copyright"],
}

html_context = {
    "github_user": "common-workflow-language",
    "github_repo": "user_guide",
    "github_version": "gh-pages",
    "doc_path": "",
}
