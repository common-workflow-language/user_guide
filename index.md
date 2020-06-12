---
layout: lesson
root: .  # Is the only page that doesn't follow the pattern /:path/index.html
permalink: index.html  # Is the only page that doesn't follow the pattern /:path/index.html
---
Hello!

<!-- this is an html comment -->

{% comment %} This is a comment in Liquid {% endcomment %}

This guide will introduce you to writing tool wrappers and workflows using the Common Workflow Language (CWL). This guide describes the stable specification, version 1.0. Updates to the guide for more recent versions are ongoing.

> ## Contributions and Feedback are Welcome!
> This document is a work in progress. Not all features are covered, yet.
> If you find that something is missing from this guide,
> or if you'd like to provide other feedback,
> we would be delighted if you would file an Issue on the
> [project repository for this guide][repo].
> You can also suggest changes directly
> by clicking the "Edit on GitHub" button at the top-right
> of the relevant page.
{: .callout}

> ## Prerequisites
>
> * A text editor
>
> * A CWL runner. It is recommended to start with the [reference implementation][cwltool-install]. The full list of CWL runners is on [the project homepage][cwl-runners-list].
{: .prereq}

You also may be interested in:
1. [A quick tutorial for the subset of YAML used in CWL]({{ page.root }}{% link _extras/yaml.md %})
2. [CWL Recommended Practices]({{ page.root }}{% link _extras/recommended-practices.md %})
3. [Miscellaneous CWL tips]({{ page.root }}{% link _extras/miscellaneous.md %})

[cwl-runners-list]: https://www.commonwl.org/#Implementations
[cwltool-install]: https://github.com/common-workflow-language/cwltool#install
[repo]: https://github.com/common-workflow-language/user_guide/issues
{% include links.md %}
