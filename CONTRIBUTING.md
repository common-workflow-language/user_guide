# Contributing

The [Common Workflow Language project][cwl-site] is an open source project,
and we welcome contributions of all kinds:
new sections,
fixes to existing material,
bug reports,
and reviews of proposed changes are all welcome.

## Contributor Agreement

By contributing,
you agree that we may redistribute your work under [our license](/LICENSE.md).
In exchange,
we will address your issues and/or assess your change proposal as promptly as we can,
and help you become a member of our community.
Everyone involved in the [Common Workflow Language project][cwl-site]
agrees to abide by our [code of conduct](/CODE_OF_CONDUCT.md).

## How to Contribute

The easiest way to get started is to file an issue
to tell us about a spelling mistake,
some awkward wording,
or a factual error.
This is a good way to introduce yourself
and to meet some of our community members.

1. If you do not have a [GitHub][github] account,
    you can [send us comments by email][discuss-list].
    However,
    we will be able to respond more quickly if you use one of the other methods described below.

2. If you have a [GitHub][github] account,
    or are willing to [create one][github-join],
    but do not know how to use Git,
    you can report problems or suggest improvements by [creating an issue][issues].
    This allows us to assign the item to someone
    and to respond to it in a threaded discussion.

3. If you are comfortable with Git,
    and would like to add or change material,
    you can submit a pull request (PR).
    Instructions for doing this are [included below][using-github].

4. To build and run the user guide locally, see **Building** below

**Note:** The published version of the user guide <https://www.commonwl.org/user_guide/> is built from the `release` branch.
New changes are gathered on the default (`main`) branch which is built at <https://common-workflow-languageuser-guide.readthedocs.io/en/latest/>
as a preview. Once we collect many changes from the `main` branch, we merge them into the `release` branch.


Pull requests include an automatic preview provided by
[ReadTheDocs](https://readthedocs.org/projects/common-workflow-languageuser-guide/).

## What to Contribute

There are many ways to contribute,
like updating or filling in the documentation
and submitting [bug reports][issues]
about things that don't work, aren't clear, or are missing.
If you are looking for ideas,
please see [the list of issues for this repository][issues],
or the issues for [Common Workflow Language][cwl-issues] project itself.

Comments on issues and reviews of pull requests are just as welcome:
we are smarter together than we are on our own.
Reviews from novices and newcomers are particularly valuable:
it's easy for people who have been using these materials for a while
to forget how impenetrable some of this material can be,
so fresh eyes are always welcome.

## Using GitHub

If you choose to contribute via GitHub, you may want to look at
[How to Contribute to an Open Source Project on GitHub][how-contribute].
To manage changes, we follow [GitHub flow][github-flow].
To use the web interface for contributing:

1.  Fork the originating repository to your GitHub profile.
2.  Within your version of the forked repository, move to the `main` branch and
create a new branch for each significant change being made.
3.  Navigate to the file(s) you wish to change within the new branches and make revisions as required.
4.  Commit all changed files within the appropriate branches.
5.  Create individual pull requests from each of your changed branches
to the `main` branch within the originating repository.
6.  If you receive feedback, make changes using your issue-specific branches of the forked
repository and the pull requests will update automatically.
7.  Repeat as needed until all feedback has been addressed.

When starting work, please make sure your clone of the originating `main` branch is up-to-date
before creating your own revision-specific branch(es) from there.
Additionally, please only work from your newly-created branch(es) and *not*
your clone of the originating `main` branch.
Lastly, published copies of all the sections are available in the `main` branch of the originating
repository for reference while revising.

## Building

The user guide uses [Sphinx](https://www.sphinx-doc.org/), a Python documentation
tool. You must have a recent version of Python 3.6+ installed to build the project
locally. It is also recommended having `make` (otherwise look at the commands used
in `Makefile`).

The `dot` program from Graphviz is needed to render some of the diagrams.

* For Debian/Ubuntu users:
```bash
sudo apt-get install graphviz
```
* For non-Debian/Ubuntu users, follow the directions at [the GraphViz download site](https://graphviz.org/download).
```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
# update the version of pip, setuptools, and wheel
(venv) pip install -U pip setuptools wheel
# Install all the dependencies in your virtual environment.
(venv) pip install ".[all]"
# Create the HTML to visualize locally
(venv) make html
(venv) open _build/html/index.html
# Or you can start a serve that watches for local file changes
(venv) make watch
# Open <http://localhost:8000/> in your browser
```

> NOTE: When you modify the packages installed with apt or pip, please verify
> if the change needs to be applied to either or to both of CI and readthedocs.
> ReadTheDocs builds and deploys previews. CI builds and deploys production
> (GitHub Actions). Failing to update both may result in previews generated
> correctly, but failure to deploy the production version after the pull request
> gets merged.

## Style Guide

We must use the phrase "CWL standards" or "CWL open standards" when talking about CWL.
We must use the word "specification" only when talking specifically about the CWL
specification document.

Whenever a page is updated we must verify that it does not break existing
links, both internal and external. The `make html` command will fail if Sphinx detects broken links.
It only works for links managed by Sphinx (i.e. table of contents links,
or links to Markdown pages). For simple HTML links (e.g. `< href=>` or
markdown external links) pull request reviewers must verify that links
are still working after the change.

Use “tool description” not “tool wrapper” for describing the first argument
given to the `cwl-runner` or `cwltool` commands.

### Code Examples

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

### Creating Links

Sphinx and the theme are configured to auto-generate anchor slug
links for sections. So sections like ``## cwl standard`` are translated
into an anchor link `#cwl-standard`.

If you are having trouble with links to sections or code blocks, it might
be due to duplicated sections, or to spaces or other characters. To
preview the generated links, use the `myst-anchors` tool.

## Other Resources

General discussion of [Common Workflow Language][cwl-site] project
happens on the [discussion mailing list][discuss-list],
which everyone is welcome to join.

[discuss-list]: https://groups.google.com/forum/#!forum/common-workflow-language
[github]: https://github.com
[github-flow]: https://guides.github.com/introduction/flow/
[github-join]: https://github.com/join
[how-contribute]: https://docs.github.com/en/get-started/quickstart/contributing-to-projects
[issues]: https://github.com/common-workflow-language/user_guide/issues
[cwl-issues]: https://github.com/common-workflow-language/common-workflow-language/issues
[repo]: https://github.com/common-workflow-language/user_guide
[cwl-site]: https://www.commonwl.org/
[using-github]: https://docs.github.com/en/get-started/
