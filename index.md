---
layout: lesson
root: .  # Is the only page that doesn't follow the pattern /:path/index.html
permalink: index.html  # Is the only page that doesn't follow the pattern /:path/index.html
---
Hello!

<!-- this is an html comment -->

{% comment %} This is a comment in Liquid {% endcomment %}

This guide will introduce you to writing tool wrappers and workflows using the Common Workflow Language (CWL). This guide describes the current stable specification, version 1.0.

Note: This document is a work in progress. Not all features are covered, yet.

> ## Prerequisites
>
> A text editor
>
> A CWL runner. It is recommended to start with the [reference implementation][cwltool-install]. The full list of CWL runners is on [the project homepage][cwl-runners-list].
{: .prereq}

[cwl-runners-list]: https://www.commonwl.org/#Implementations
[cwltool-install]: https://github.com/common-workflow-language/cwltool#install
{% include links.md %}
