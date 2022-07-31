# Basic Concepts

This section describes the basic concepts for users to get started working with
Common Workflow Language (CWL) workflows. Readers are expected to be familiar
with workflow managers, YAML, and comfortable following instructions for the
command-line. The other sections of the user guide cover the same concepts but
in more detail. If you are already familiar with CWL or looking for more advanced
content, you may want to skip this section.

## The CWL specification

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

## Implementations

An implementation of the CWL specification is any software written following
what is defined in a version of the specification document. Implementations may
not implement every aspect of the specification. CWL implementations are
licensed under both Open Source and commercial licenses.

CWL is well suited for describing large-scale workflows in cluster,
cloud and high performance computing environments where tasks are scheduled
in parallel across many nodes.

% TODO: add a link to the Core Concepts -> Requirements section below?

## Requirements

The CWL specification allows for implementations to provide extra
functionality and specify prerequisites to workflows through *requirements*.
There are many requirements defined in the CWL specification, for instance:

- `InlineJavascriptWorkflow`
- `SubworkflowFeatureRequirement`
- `InitialWorkDirRequirement`
- `DockerRequirement`

Some CWL runners may provide requirements that are not in the specification.
For example, GPU requirements are supported in `cwltool` through the
`cwltool:CUDARequirement`, but it is not part of the {{ cwl_version }}
specification, and won't be supported by every CWL runner.

Implementations may also decide to implement only a few requirements. For
example, if you want to use sub-workflows, first you may want to confirm
that the CWL runner you are using supports the
`SubworkflowFeatureRequirement` requirement.

Requirements are explained in detail in another section.

## Processing units

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

### Command-line tool

A command-line tool is a type of Process object that can be run by
itself or as a Workflow step. It is a wrapper for a command like
`ls`, `echo`, `tar`, etc. The command-line tool is defined in the
`baseCommand` attribute of the command-line tool CWL document.

A CWL command-line tool must also have `inputs` and `outputs`.
The following example contains a minimal example of a CWL
command-line tool for the `echo` Linux command, using inputs and
outputs.

```{graphviz}
:name: command-line-tool-graph
:caption: CWL command-line tool.
:align: center

digraph "CWL command-line tool" {
    rankdir="LR";
    graph [splines=ortho];

    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];
    inputs -> baseComand -> outputs;
}
```

```{code-block} cwl
:name: echo.cwl
:caption: "`echo.cwl`"
cwlVersion: v1.2
class: CommandLineTool

baseCommand: echo

stdout: output.txt

inputs:
  message:
    type: string
    inputBinding: {}
outputs:
  out:
    type: string
    outputBinding:
      glob: output.txt
      loadContents: true
      outputEval: $(self[0].contents)
```

```{note}

The example above uses a simplified form to define inputs and outputs.
You will learn more about in the [Inputs](core-concepts/inputs.md)
and in the [Outputs](core-concepts/outputs.md) sections.
```

### Expression tool

An expression tool is a type of Process that can be run by itself or
as a Workflow step. It executes a pure JavaScript expression. It is
meant to be used as a way to isolate complex JavaScript expressions
that need to operate on input data and produce some result as output.

Similar to the command-line tool it requires `inputs` and `outputs`.
But instead of `baseCommand`, it requires an `expression` attribute.

```{graphviz}
:name: expression-tool-graph
:caption: CWL expression tool.
:align: center

digraph "CWL command-line tool" {
    rankdir="LR";
    graph [splines=ortho];

    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];
    inputs -> expression -> outputs;
}
```

```{code-block} cwl
:name: uppercase.cwl
:caption: "`uppercase.cwl`"
cwlVersion: v1.2
class: ExpressionTool

requirements:
  InlineJavascriptRequirement: {}

inputs:
  message: string
outputs:
  uppercase_message: string

expression: |
  ${ return {"uppercase_message": inputs.message.toUpperCase()}; }
```

```{note}

We had to use an `InlineJavascriptRequirement` as our expression
contains a JavaScript call in `.toUpperCase()`. This means to tools
using the expression tool that JavaScript is a requirement.
```

### Workflow

A workflow is a CWL processing unit that executes command-line tools,
expression tools, or workflows (sub-workflows) as steps. It must have
`inputs`, `outputs`, and `steps` defined in the CWL document.

```{graphviz}
:name: workflow-graph
:caption: CWL workflow.
:align: center

digraph "CWL Inputs, Steps, and Outputs" {
    rankdir="LR";
    graph [splines=ortho];

    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];
    inputs -> steps -> outputs;
}
```

The CWL document `echo-uppercase.cwl` defines a workflow that runs
the command-line tool, and the expression tool showed in the earlier
examples.

```{code-block} cwl
:name: echo-uppercase.cwl
:caption: "`echo-uppercase.cwl`"
cwlVersion: v1.2
class: Workflow

requirements:
  InlineJavascriptRequirement: {}

inputs:
  message: string

outputs:
  out:
    type: string
    outputSource: uppercase/uppercase_message

steps:
  echo:
    run: echo.cwl
    in:
      message: message
    out: [out]
  uppercase:
    run: uppercase.cwl
    in:
      message:
        source: echo/out
    out: [uppercase_message]
```

A command-line tool or expression tool can also be written directly
in the same CWL document as the workflow. For example, we can rewrite
the `echo-uppercase.cwl` workflow as a single file:

```{code-block} cwl

:name: echo-uppercase-single-file.cwl
:caption: "`echo-uppercase-single-file.cwl`"
cwlVersion: v1.2
class: Workflow

requirements:
  InlineJavascriptRequirement: {}

inputs:
  message: string

outputs:
  out:
    type: string
    outputSource: uppercase/uppercase_message

steps:
  echo:
    run:
      class: CommandLineTool

      baseCommand: echo

      stdout: output.txt

      inputs:
        message:
          type: string
          inputBinding: {}
      outputs:
        out:
          type: string
          outputBinding:
            glob: output.txt
            loadContents: true
            outputEval: $(self[0].contents)
    in:
      message: message
    out: [out]
  uppercase:
    run:
      class: ExpressionTool

      requirements:
        InlineJavascriptRequirement: {}

      inputs:
        message: string
      outputs:
        uppercase_message: string

      expression: |
        ${ return {"uppercase_message": inputs.message.toUpperCase()}; }
    in:
      message:
        source: echo/out
    out: [uppercase_message]
```

Having separate files helps with modularity and code organization. But
it can be helpful writing everything in a single file for development.
There are other ways to combine multiple files into a single file
(e.g. `cwltool --pack`) discussed further in other sections of this
user guide.

% TODO: add a link to the page about SubworkflowFeatureRequirement

```{note}

For a sub-workflows you need to enable the requirement
`SubworkflowFeatureRequirement`. It is covered in another section
of this user guide in more detail.
```

## FAIR workflows

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

## Learn more

- The CWL Specification page in the CWL website: <https://www.commonwl.org/specification/>
- The current CWL specification on GitHub: {{ '<https://github.com/common-workflow-language/cwl-{}>'.format(cwl_version_text) }}
- The list of Implementations in the CWL website: <https://www.commonwl.org/implementations/>
- Semantic Versioning - <https://semver.org/>
