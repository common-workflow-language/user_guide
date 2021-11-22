---
title: Setup
---
To follow the Common Workflow Language user guide, you will need an up-to-date
Linux or Mac OS X system, with the following software installed:

- A text editor with YAML support, for example [Visual Studio Code with the Benten (CWL) plugin](https://github.com/rabix/benten#install-vs-code-extension). There's a complete list of plugins that add CWL support to code editors at https://www.commonwl.org/#Editors_and_viewers
- A CWL implementation to run the described tools and workflows. When first
getting started with CWL, we recommend the reference implementation,
[`cwltool`][ref-imp]. You can find a full list on
[the project homepage][commonwl].
- Most of the software tools used in the user guide are standard UNIX commands
(`cat`, `echo`, `env`, `tar`, `touch`, `wc`), but to run all examples you will
also need:
  - node.js
  - Java compiler
  - Docker (optional)

[ref-imp]: https://github.com/common-workflow-language/cwltool#install
[commonwl]: https://www.commonwl.org/
{% include links.md %}
