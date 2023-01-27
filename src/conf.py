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
    'sphinx.ext.graphviz',
    'sphinx_reredirects',
    'cwl.sphinx.runcmd'
]

# myst-parser settings
myst_heading_anchors = 4
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'substitution',
    'replacements',
]
CWL_VERSION = 'v1.2'
myst_substitutions = {
    'repo_url': 'https://github.com/common-workflow-language/user_guide/',
    'source_branch': 'main',
    'cwl_version': f'`{CWL_VERSION}`',
    'cwl_version_text': f'{CWL_VERSION}'
}

master_doc = 'index'

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
    '**/Thumbs.db',
    '**/.DS_Store',
    '**/.git',
    '.idea',
    '.github',
    '**/_build',
    '**/_includes',
    'cwl',
    'venv',
    'README.md',
    'CODE_OF_CONDUCT.md',
    'CONTRIBUTING.md'
]

source_suffix = ['.rst', '.md']

# -- Options for URL redirects -----------------------------------------------

redirects = {
    '01-introduction/index.md': '../introduction/quick-start.html',
    '02-1st-example/index.md': '../introduction/quick-start.html',
    '03-input/index.md': '../topics/inputs.html',
    '04-output/index.md': '../topics/outputs.html',
    '05-stdout/index.md': '../topics/outputs.html',
    '06-params/index.md': '../topics/parameter-references.html',
    '07-containers/index.md': '../topics/using-containers.html',
    '08-arguments/index.md': '../topics/additional-arguments-and-parameters.html',
    '09-array-inputs/index.md': '../topics/inputs.html',
    '10-array-outputs/index.md': '../topics/outputs.html',
    '11-records/index.md': '../topics/inputs.html',
    '12-env/index.md': '../topics/environment-variables.html',
    '13-expressions/index.md': '../topics/expressions.html',
    '14-runtime/index.md': '../topics/creating-files-at-runtime.html',
    '15-staging/index.md': '../topics/staging-input-files.html',
    '16-file-formats/index.md': '../topics/file-formats.html',
    '17-metadata/index.md': '../topics/metadata-and-authorship.html',
    '19-custom-types/index.md': '../topics/custom-types.html',
    '20-software-requirements/index.md': '../topics/specifying-software-requirements.html',
    '21-1st-workflow/index.md': '../topics/workflows.html',
    '22-nested-workflows/index.md': '../topics/workflows.html#nested-workflows',
    '23-scatter-workflow/index.md': '../topics/workflows.html#scattering-workflows',
    '24_conditional-workflow/index.md': '../topics/workflows.html#conditional-workflows',
    'rec-practices/index.md': '../topics/best-practices.html',
    'misc/index.md': '../faq.html',
    'episodes.md': 'index.html#table-of-contents',
    'setup.md': 'introduction/prerequisites.html',
    'extras.md': '/index.html',
    'yaml/index.md': '../topics/yaml-guide.html',
    'CODE_OF_CONDUCT.html': 'https://github.com/common-workflow-language/user_guide/blob/main/CODE_OF_CONDUCT.md'
}

# -- Options for Pygments ----------------------------------------------------

pygments_style = 'default'

# TODO: maybe write our own lexer to customize tokens, keywords, etc?
lexers['cwl'] = YamlLexer()

highlight_options = {
  'default': {
      'stripall': True
  }
}

# -- GraphViz configuration --------------------------------------------------

from cwl.doc.graphs import create_processing_units_graph

graphviz_output_format = 'svg'

myst_substitutions['CWL_PROCESSING_UNITS_GRAPH'] = create_processing_units_graph()

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

html_logo = '_static/images/logos/cwl/CWL-Logo-HD-cropped2.png'
html_favicon = '_static/images/favicons/cwl/favicon.ico'

html_extra_path = [
    'browserconfig.xml',
    'favicon.ico',
    'manifest.json'
]

html_theme_options = {
    "external_links": [
      {"name": "Community", "url": "https://www.commonwl.org/community/"},
    ],
    "header_links_before_dropdown": 6,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/common-workflow-language/user_guide/",
            "icon": "fab fa-github-square",
        },
    ],
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": version_match,
    # },
    "use_edit_page_button": True,
    "navbar_align": "content",
    "navbar_end": [
        # "version-switcher",
        "theme-switcher",
        "navbar-icon-links"
    ],
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
    "github_version": "main",
    "doc_path": "src",
    "default_mode": "light"
}

gettext_uuid = True
gettext_compact = "user_guide"
locale_dirs = ['../locales/']


# Patched MyST parser
# from __future__ import annotations

from docutils import nodes
from docutils.parsers.rst import Parser as RstParser
from sphinx.parsers import Parser as SphinxParser
from sphinx.util import logging

from myst_parser.config.main import (
    MdParserConfig,
    TopmatterReadError,
    merge_file_level,
    read_topmatter,
)
from myst_parser.mdit_to_docutils.sphinx_ import SphinxRenderer, create_warning
from myst_parser.parsers.mdit import create_md_parser

SPHINX_LOGGER = logging.getLogger(__name__)

class MystParser(SphinxParser):
    """Sphinx parser for Markedly Structured Text (MyST)."""

    supported: tuple[str, ...] = ("md", "markdown", "myst")
    """Aliases this parser supports."""

    settings_spec = RstParser.settings_spec
    """Runtime settings specification.
    Defines runtime settings and associated command-line options, as used by
    `docutils.frontend.OptionParser`.  This is a concatenation of tuples of:
    - Option group title (string or `None` which implies no group, just a list
      of single options).
    - Description (string or `None`).
    - A sequence of option tuples
    """

    config_section = "myst parser"
    config_section_dependencies = ("parsers",)
    translate_section_name = None

    def parse(self, inputstring: str, document: nodes.document) -> None:
        """Parse source text.
        :param inputstring: The source string to parse
        :param document: The root docutils node to add AST elements to
        """
        # get the global config
        config: MdParserConfig = document.settings.env.myst_config

        # update the global config with the file-level config
        try:
            topmatter = read_topmatter(inputstring)
        except TopmatterReadError:
            pass  # this will be reported during the render
        else:
            if topmatter:
                warning = lambda wtype, msg: create_warning(  # noqa: E731
                    document, msg, line=1, append_to=document, subtype=wtype
                )
                config = merge_file_level(config, topmatter, warning)

        parser = create_md_parser(config, SphinxRenderer)
        # TODO: In the first pass, the call above will use MarkdownIt over the whole document,
        #       populating the ``.md_env`` correctly. Over the next passes, from transforms as
        #       ``sphinx.transforms.i18n.Locale`` it will create a blank new document, as well
        #       as a new MarkdownIT parser but using just the Docutils document that is being
        #       translated. As a result of this, the translation has no reference-links, and it
        #       gives you the translation without resolving the links. Here we just re-use the
        #       ``md_env`` dictionary that contains the ``.references`` populated in the first
        #       pass, fixing i18n with MyST Parser.
        env = {} if not hasattr(document.settings, 'md_env') else document.settings.md_env
        parser.options["document"] = document
        parser.render(inputstring, env)
        document.settings.md_env = parser.renderer.md_env


def setup(app):
    """Sphinx setup callback."""

    # TODO: Here we replace the MySTParser (that replaces the Sphinx default parser...),
    #       with our patched version above.
    app.add_source_parser(MystParser, override=True)
