# Introduction

## Quick Start

This section will show you a brief overview of what is CWL and where you
can learn more about it. No previous knowledge of CWL is required, but you
must be comfortable following instructions for the command-line.

### “Hello World”

```{include} /_includes/what-is-cwl.md
```

CWL documents are written in [YAML](yaml/index.md) (and/or JSON).
The example below shows a simple CWL “Hello World” workflow annotated
with comments:

```{literalinclude} /_includes/cwl/hello_world.cwl
:language: cwl
:name: hello_world.cwl
:caption: "`hello_world.cwl`"
```

The example above is just a wrapper for the `echo` command-line tool.
Running the workflow above with the default input values, produces the
command-line `echo "Hello World"`.

```{note}
There is a distinction in CWL between a command-line tool and a workflow. But
for the sake of simplicity we are using the term “workflow” here. You will learn
more about this in the [basic concepts](#basic-concepts) section.
```

### Installing a CWL runner

`cwltool` is an implementation of the CWL specification. It is also the
CWL *Reference Runner* for the specification, and compliant with the
latest version of the specification, {{ cwl_version }}. You can install
`cwltool` using `pip`:

```{code-block} console
:name: installing-cwltool-with-pip
:caption: Installing `cwltool` with `pip`.

$ pip install cwltool
```

```{note}
The [prerequisites](#prerequisites) section contains a more detailed list
of software and libraries used for following the rest of this user guide.
It also contains other ways to install `cwltool`.
```

### Running "Hello World"

The usage of the `cwltool` command-line executable is basically
`cwltool [OPTIONS] <CWL_DOCUMENT> [INPUTS_OBJECT]`. You can run the
`hello_world.cwl` workflow without specifying any option:

```{code-block} console
:name: running-hello_world.cwl-with-cwltool
:caption: Running `hello_world.cwl` with `cwltool`.

$ cwltool hello_world.cwl
INFO /tmp/venv/bin/cwltool 3.1.20220628170238
INFO Resolved 'hello_world.cwl' to 'file:///tmp/hello_world.cwl'
INFO [job hello_world.cwl] /tmp/yn0e8xu6$ echo \
    'Hello World'
Hello World
INFO [job hello_world.cwl] completed success
{}
INFO Final process status is success
```

Or you can override the default value of the input parameter `message`, similar
to how you would change the argument of the `echo` base command:

```{code-block} console
:name: running-hello_world.cwl-with-cwltool-passing-an-input-parameter
:caption: Running `hello_world.cwl` with `cwltool` passing an input parameter.

$ cwltool hello_world.cwl --message="Hola mundo"
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220406080846
INFO Resolved '/tmp/hello_world.cwl' to 'file:///tmp/hello_world.cwl'
INFO [job hello_world.cwl] /tmp/ua5vt9hl$ echo \
    'Hola mundo'
Hola mundo
INFO [job hello_world.cwl] completed success
{}
INFO Final process status is success
```

Another way of passing values to your workflow input parameters is via an
*Inputs Object*. This is a file containing the input fields with the
corresponding values. This file can be written in JSON or YAML. For example:

```{code-block} json
:name: hello_world-job.json
:caption: "`hello_world-job.json`"
{
  "message": "こんにちは世界"
}
```
<p class="text-center text-muted mt-n2">hello_world-job.json</p>

You can use this Inputs Object file now to execute the “Hello World” workflow:

```{code-block} console
:name: passing-an-inputs-object-file-to-cwltool
:caption: Passing an Inputs Object file to `cwltool`.
$ cwltool hello_world.cwl hello_world-job.json
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220406080846
INFO Resolved '/tmp/hello_world.cwl' to 'file:///tmp/hello_world.cwl'
INFO [job hello_world.cwl] /tmp/c5uchknw$ echo \
    こんにちは世界
こんにちは世界
INFO [job hello_world.cwl] completed success
{}
INFO Final process status is success
```

```{note}
We used a similar file name for the workflow and for the inputs object files.
The *-job.json* suffix is very common in Inputs Object files, but it is not
a requirement. You can choose any name for your workflows and inputs object
files.
```

### Learn more

- Continue reading the next sections of this User Guide!
- List of CWL Implementations: <https://www.commonwl.org/implementations/>
- The `common-workflow-language` organization at GitHub: <https://github.com/common-workflow-language>
- Common Workflow Language at Wikipedia: <https://en.wikipedia.org/wiki/Common_Workflow_Language>
- YAML.org: <http://yaml.org/> and YAML at Wikipedia: <https://en.wikipedia.org/wiki/YAML>
- The CWL {{ cwl_version  }} Specification: {{ '<https://www.commonwl.org/{}/>'.format(cwl_version_text) }}
- Workflow management system at Wikipedia: <https://en.wikipedia.org/wiki/Workflow_management_system>

% N.B.: Wondering what's up with this syntax in the CWL Specification link above?
% It's necessary as MyST Parser does not allow substitutions in links, for more:
% - https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-and-urls
% - https://github.com/executablebooks/MyST-Parser/issues/279

## Prerequisites

% This page supersedes the old setup.md. We used that page as reference while
% writing this documentation.

The software and configurations listed in this section are prerequisites for
following this user guide. The CWL Specification is implemented by multiple
CWL Runners. This list of requirements focuses on the `cwltool` runner. You
can use another CWL Runner but the examples may produce a different output.

```{admonition} CWL Implementations

There are many CWL Implementations. Some are complete CWL Runners,
others are plug-ins or extensions to Workflow Engines. We have a better
explanation in the [Implementations](#implementations) section.
```

### Operating System

We recommend using an up-to-date operating system. You can choose any
of the following options for your operating system:

- Linux
- macOS

You can try to use Window Subsystem for Linux 2 (WSL) to follow the
User Guide documentation, but some examples may not work as expected.

Your operating system also needs Internet access and a recent version
of Python 3.

### CWL runner

% https://github.com/common-workflow-language/user_guide/issues/166
% https://github.com/common-workflow-language/user_guide/issues/64
% https://www.synapse.org/#!Synapse:syn2813589/wiki/401462

The first thing you will need for running CWL workflows is a CWL runner.
`cwltool` is a Python Open Source project maintained by the CWL community. It
is also the CWL reference runner, which means it must support everything in the
current CWL specification, {{ cwl_version }}.

`cwltool` can be installed with `pip`. We recommend using a virtual environment
like `venv` or `conda`. The following commands will create and activate a Python
virtual environment using the `venv` module, and install `cwltool` in that
environment:

```{code-block} console
:name: installing-cwltool-with-pip-and-venv
:caption: Installing `cwltool` with `pip` and `venv`.

$ python -m venv venv
$ source venv/bin/activate
$ (venv) pip install cwltool
```

```{note}
Visit the `cwltool` [documentation](https://github.com/common-workflow-language/cwltool#install)
for other ways to install `cwltool` with `apt` and `conda`.
```

Let's use a simple workflow `true.cwl` with `cwltool`.

```{literalinclude} /_includes/cwl/simplest_cwl.cwl
:language: cwl
:caption: "`true.cwl`"
:name: true.cwl
```

The `cwltool` command has an option to validate CWL workflows. It will parse the
CWL workflow, look for syntax errors, and verify that the workflow is compliant
with the CWL specification, without running the workflow. To use it you just need
to pass `--validate` to the `cwltool` command:

% TODO: maybe figure out a way to avoid /home/kinow/ etc. in the documentation
%       to avoid multiple user-names/directory-locations varying in the docs.

```{code-block} console
:name: validating-truecwl-with-cwltool
:caption: Validating `true.cwl` with `cwltool`.

$ cwltool --validate true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220406080846
INFO Resolved 'true.cwl' to 'file:///tmp/true.cwl'
true.cwl is valid CWL.
```

You can run the CWL workflow now that you know it is valid:

```{code-block} console
:name: running-true.cwl-with-cwltool
:caption: Running `true.cwl` with `cwltool`.

$ cwltool true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220406080846
INFO Resolved 'true.cwl' to 'file:///tmp/true.cwl'
INFO [job true.cwl] /tmp/f8xlh1pl$ true
INFO [job true.cwl] completed success
{}
INFO Final process status is success
```

#### cwl-runner Python module

`cwl-runner` is an implementation agnostic alias for CWL Runners.
Users can invoke `cwl-runner` instead of invoking a CWL runner like `cwltool`
directly. The `cwl-runner` alias command then chooses the correct CWL runner.
This is convenient for environments with multiple CWL runners.

The CWL community publishes a Python module with the same name,
`cwl-runner`, that defaults to `cwltool`. `cwl-runner` will be used in
the rest of this user guide. You can use `pip` to install the `cwl-runner`
Python module:

```{code-block} console
:name: installing-cwlrunner-with-pip
:caption: Installing `cwl-runner` with `pip`.

$ pip install cwl-runner
```

% TODO: Maybe tell users where the cwl-runner source is? I couldn't find in PYPI as
%       it points to the CWL project: https://github.com/common-workflow-language/cwltool/tree/main/cwlref-runner

Now you can validate and run your workflow with `cwl-runner` executable,
which will invoke `cwltool`. You should have the same results and output
as in the previous section.

```{code-block} console
:name: validating-true.cwl-with-cwl-runner
:caption: Validating `true.cwl` with `cwl-runner`.

$ cwl-runner --validate true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwl-runner 3.1.20220406080846
INFO Resolved 'true.cwl' to 'file:///tmp/true.cwl'
true.cwl is valid CWL.
```

```{code-block} console
:name: running-true.cwl-with-cwl-runner
:caption: Running `true.cwl` with `cwl-runner`.

$ cwl-runner true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwl-runner 3.1.20220406080846
INFO Resolved 'true.cwl' to 'file:///tmp/true.cwl'
INFO [job true.cwl] /tmp/7a2gf1nh$ true
INFO [job true.cwl] completed success
{}
INFO Final process status is success
```

Another way to execute `cwl-runner` is invoking the file directly. For that,
the first thing you need is to modify the `true.cwl` workflow and include
a special first line, a *shebang*:

```{literalinclude} /_includes/cwl/simplest_cwl_shebang.cwl
:language: cwl
:name: cwltool-with-a-shebang
:caption: "`cwltool` with a shebang"
```

Now, after you make the file `true.cwl` executable with `chmod u+x`,
you can execute it directly in the command-line and the program
specified in the shebang (`cwl-runner`) will be used to execute the
rest of the file.

```{code-block} console
:name: making-true.cwl-executable-and-running-it
:caption: Making `true.cwl` executable and running it.

$ chmod u+x true.cwl
$ ./true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwl-runner 3.1.20220406080846
INFO Resolved './true.cwl' to 'file:///tmp/true.cwl'
INFO [job true.cwl] /tmp/jz7ups99$ true
INFO [job true.cwl] completed success
{}
INFO Final process status is success
```

```{note}
The *shebang* is the two-character sequence `#!` at the beginning of a
script. When the script is executable, the operating system will execute
the script using the executable specified after the shebang. It is
considered a good practice to use `/usr/bin/env <executable>` since it
looks for the `<executable>` program in the system `PATH`, instead of
using a hard-coded location.
```

### Text Editor

You can use any text editor with CWL, but for syntax highlighting we recommend
an editor with YAML support. Popular editors are Visual Studio Code, Sublime,
WebStorm, vim/neovim, and Emacs.

There are extensions for Visual Studio Code and WebStorm that provide
integration with CWL, with customized syntax highlighting and better
auto-complete:

- Visual Studio Code with the Benten (CWL) plugin - <https://github.com/rabix/benten#install-vs-code-extension>
- cwl-plugin for IntelliJ - <https://plugins.jetbrains.com/plugin/10040-cwl-plugin>

The CWL community also maintains a list of editors and viewers:
<https://www.commonwl.org/#Editors_and_viewers>

### Docker

% https://github.com/common-workflow-language/user_guide/issues/119

`cwltool` uses Docker to run workflows or workflow steps with containers.
Follow the instructions in the Docker documentation to install it for your
operating system: <https://docs.docker.com/>.

You do not need to know how to write and build Docker containers. In the
rest of the user guide we will use existing Docker images for running
examples, and to clarify the differences between the execution models
with and without containers.

```{note}
`cwltool` supports running containers with Docker, Podman, udocker, and
Singularity. You can also use alternative container registries for pulling
images.
```

### Learn more

- The [Implementations](#implementations) topic in the next section, Basic Concepts.
- The Python `venv` module: <https://docs.python.org/3/library/venv.html>

## Basic Concepts

This section describes the basic concepts for users to get started working with
Common Workflow Language (CWL) workflows. Readers are expected to be familiar
with workflow managers, YAML, and comfortable following instructions for the
command-line. The other sections of the user guide cover the same concepts but
in more detail. If you are already familiar with CWL or looking for more advanced
content, you may want to skip this section.

### The CWL specification

```{include} /_includes/what-is-cwl.md
```

```{image} /_static/images/logos/cwl/CWL-Logo-HD-cropped2.png
:name: cwl-logo
:width: 300px
:align: center
```

The CWL specification is a document written and maintained by the CWL community.
The specification has different versions. The version covered in this user guide
is the {{ cwl_version }}.

The specification version can have up to three numbers separated by `.`'s (dots).
The first number is the major release, used for backward-incompatible changes like
the removal of deprecated features. The second is the minor release number,
used for new features or smaller changes that are backward-compatible. The last number
is used for bug fixes, like typos and other corrections to the specification.

```{note}

The model used for the specification version is called Semantic Versioning. See
the end of this section to [learn more](#learn-more) about it.
```

### Implementations

An implementation of the CWL specification is any software written following
what is defined in a version of the specification document. Implementations may
not implement every aspect of the specification. CWL implementations are
licensed under both Open Source and commercial licenses.

CWL is well suited for describing large-scale workflows in cluster,
cloud and high performance computing environments where tasks are scheduled
in parallel across many nodes.

% TODO: add a link to the Core Concepts -> Requirements section below?

```{graphviz}
:name: specification-and-implementations-graph
:caption: CWL specification, implementations, and other tools.
:align: center

digraph G {
    compound=true;
    rankdir="LR";
    ranksep=0.75;
    fontname="Verdana";
    fontsize="10";
    graph [splines=ortho];
    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];
    subgraph cluster_0 {
        label="Implementations";
        ranksep=0.25;

        cwltool;
        toil;
        Arvados;
        runner_others[label="..."];
        label="CWL Runners";
    }

    subgraph cluster_1 {
        label="Tools";
        ranksep=0.25;

        subgraph cluster_2 {
            "vscode-cwl";
            "vim-cwl";
            benten;
            editor_others[label="..."];
            label="Editors";
        }

        subgraph cluster_3 {
            "CWL Viewer";
            "vue-cwl";
            viewer_others[label="..."];
            label="Viewers";
        }

        "And more";
    }
    cwltool -> "CWL Specification" [ltail=cluster_0, dir=back];
    "CWL Specification" -> "vscode-cwl" [lhead=cluster_1];
    "vscode-cwl" -> "CWL Viewer" [style=invis];
    "CWL Viewer" -> "And more" [style=invis];
}

```

### Requirements

The CWL specification allows for implementations to provide extra
functionality and specify prerequisites to workflows through *requirements*.
There are many requirements defined in the CWL specification, for instance:

- `InlineJavascriptWorkflow`
- `SubworkflowFeatureRequirement`
- `InitialWorkDirRequirement`
- `DockerRequirement`

Some CWL runners may provide requirements that are not in the specification.
For example, GPU requirements are supported in `cwltool` through the
`cwltool:CUDARequirement` requirement, but it is not part of the
{{ cwl_version }} specification and may not be supported by other CWL
runners.

Implementations may also decide to implement only a few requirements. For
example, if you want to use sub-workflows, first you may want to confirm
that the CWL runner you are using supports the
`SubworkflowFeatureRequirement` requirement.

Requirements are explained in detail in another section.

### Processing units

There are four types of processing units defined in the CWL specification
{{ cwl_version }}:

- A command-line tool;
- An expression tool;
- An operation;
- And a workflow.

{{ CWL_PROCESSING_UNITS_GRAPH }}

In `cwltool` you can execute a CWL document with a command-line tool,
an expression tool, or a workflow. Operation is a special unit, not
covered in this section.

You define the processing unit in your CWL document using the
`class` attribute, e.g. `class: Workflow`.

#### Command-line tool

```{include} /_includes/command-line-tool.md
```

#### Expression tool

```{include} /_includes/expression-tool.md
```

#### Workflow

```{include} /_includes/workflow.md
```

### FAIR workflows

> The FAIR principles have laid a foundation for sharing and publishing
> digital assets and, in particular, data. The FAIR principles emphasize
> machine accessibility and that all digital assets should be Findable,
> Accessible, Interoperable, and Reusable. Workflows encode the methods
> by which the scientific process is conducted and via which data are
> created. It is thus important that workflows both support the creation
> of FAIR data and themselves adhere to the FAIR principles.
> — [FAIR Computational Workflows](https://workflows.community/groups/fair/),
> Workflows Community Initiative.

CWL has roots in "make" and many similar tools that determine order of
execution based on dependencies between tasks. However, unlike "make", CWL
tasks are isolated, and you must be explicit about your inputs and outputs.

The benefit of explicitness and isolation are flexibility, portability, and
scalability: tools and workflows described with CWL can transparently leverage
technologies such as Docker and be used with CWL implementations from different
vendors.

`cwltool` also uses the PROV-O standard ontology for data provenance.

### Learn more

- Semantic Versioning - <https://semver.org/>
- The CWL Specification page in the CWL website: <https://www.commonwl.org/specification/>
- The current CWL specification on GitHub: {{ '<https://github.com/common-workflow-language/cwl-{}>'.format(cwl_version_text) }}
- The list of Implementations in the CWL website: <https://www.commonwl.org/implementations/>
- PROV-O: The PROV Ontology - <https://www.w3.org/TR/prov-o/>
- CWL Operations are covered in the [Operations](core-concepts/operations.md) section of this user guide.
