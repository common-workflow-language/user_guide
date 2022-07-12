[![DOI](https://zenodo.org/badge/89621457.svg)](https://zenodo.org/badge/latestdoi/89621457)

[![Syntax Check](https://travis-ci.org/common-workflow-language/user_guide.svg?branch=main)](https://travis-ci.org/common-workflow-language/user_guide)

[User guide for CWL v1.2.0](https://www.commonwl.org/user_guide/)

Original source:
https://github.com/common-workflow-language/common-workflow-language/blob/a2a8a08b8c8d56f8f2ca6284ca4e9cbf23d19346/v1.0/UserGuide.yml

## Contributing

We welcome all contributions to improve the materials! Maintainers will do their best to help you if you have any
questions, concerns, or experience any difficulties along the way.
To edit the user guide:

We'd like to ask you to familiarize yourself with our [Contribution Guide](CONTRIBUTING.md).

### Code examples

To include code into a Markdown file you have two options. For external files use
the following command:

````
```{literalinclude} /_includes/cwl/hello_world.cwl
:language: cwl
```
````

For code examples in the same page, you can use fence blocks.

````
```bash
echo "Hello world"
```
````

If you would like to customize the syntax highlighting styles
you will have to customize the Sphinx and Pygments settings.
To preview Pygments output with different styles, use their
[Pygments demo tool](https://pygments.org/demo/).

### Links

Sphinx and the theme are configured to auto-generate anchor slug
links for sections. So sections like ``## cwl standard`` are translated
into an anchor link `#cwl-standard`.

If you are having trouble with links to sections or code blocks, it might
be due to duplicated sections, or to spaces or other characters. To
preview the generated links, use the `myst-anchors` tool.

```bash
$ (venv) myst-anchors basic-concepts.md
<h1 id="basic-concepts"></h1>
<h2 id="the-cwl-standard"></h2>
<h2 id="implementations"></h2>
<h2 id="cwl-objects-model"></h2>
```

You can also create reference anchor links anywhere on the page with
``(test)=``, which can be used in the page as `#test` (these do not appear
in the `myst-anchor` output).

## Extensions

We use MyST Parser with Sphinx. This gives us the best of both Sphinx and Markdown,
while also supporting reStructuredText, Sphinx, and MyST extensions.

### String Substitutions

For convenience, we have the currently supported version of the specification as a
constant in `conf.py`. We have it in two forms:

- Markdown preformatted, i.e. \`v0.0\` which is formatted as `v0.0`
- Plain text, i.e. v0.0

Note that String Substitutions do not work with links. As workaround, you can use
string formatting or replacements.

```
The CWL {{ cwl_version  }} Specification: {{ '<https://www.commonwl.org/{}/>'.format(cwl_version_text) }}
```

For more:

- <https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2>
- <https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-and-urls>
- <https://github.com/executablebooks/MyST-Parser/issues/279>

## Authors

A list of contributors to these materials can be found in [AUTHORS](AUTHORS)

## Citation

To cite these materials, please consult with [CITATION](CITATION)

