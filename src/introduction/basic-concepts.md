# Basic Concepts

This section describes the basic concepts for users to get started on working with
Common Workflow Language (CWL) workflows. Readers are expected to be familiar
with workflow managers, YAML, and comfortable with following instructions for the
command-line. The other sections of the user guide cover the same concepts, but
in more detail. If you are already familiar with CWL or you are looking for more advanced
content, you may want to skip this section.

## The CWL Specification

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

The specification version can have up to three numbers separated by `.`s (dots).
The first number is the major release, used for backward-incompatible changes like
the removal of deprecated features. The second number is the minor release,
used for new features or smaller changes that are backward-compatible. The last number
is used for bug fixes, like typos and other corrections to the specification.

```{note}

The model used for the specification version is called Semantic Versioning. See
the end of this section to [learn more](#learn-more) about it.
```

## Implementations

An implementation of the CWL specification is any software written following
what is defined in a version of the specification document. However, implementations may
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

## Processes and Requirements

A process is a computing unit that takes inputs and produces outputs. The
behavior of a process can be affected by the inputs, requirements, and hints.
There are four types of processes defined in the CWL specification
{{ cwl_version }}:

- A command-line tool.
- An expression tool.
- An operation.
- A workflow.

{{ CWL_PROCESSING_UNITS_GRAPH }}

A command-line tool is a wrapper for a command-line utility like `echo`,
`ls`, and `tar`. A command-line tool can be called from a workflow.

An expression tool is a wrapper for a JavaScript expression. It can
be used to simplify workflows and command-line tools, moving common
parts of a workflow execution into reusable JavaScript code that
takes inputs and produces outputs like a command-line tool.

Operation is an abstract process that also takes inputs, produces
outputs, and can be used in a workflow. But it is a special operation
not so commonly used. It is discussed in the [Operations section](../topics/operations.md) of this user guide.

The workflow is a process that contains steps. Steps can be other
workflows (nested workflows), command-line tools, or expression tools.
The inputs of a workflow can be passed to any of its steps, while
the outputs produced by its steps can be used in the final output
of the workflow.

The CWL specification allows for implementations to provide extra
functionality and specify prerequisites to workflows through *requirements*.
There are many requirements defined in the CWL specification, for instance:

- `InlineJavascriptWorkflow` - enables JavaScript in expressions.
- `SubworkflowFeatureRequirement` - enables nested workflows.
- `InitialWorkDirRequirement` - controls staging files in the input directory.

Some CWL runners may provide requirements that are not in the specification.
For example, GPU requirements are supported in `cwltool` through the
`cwltool:CUDARequirement` requirement, but it is not part of the
{{ cwl_version }} specification and may not be supported by other CWL
runners.

Hints are similar to requirements, but while requirements list features
that are required, hints list optional features. Requirements are explained
in detail in the [Requirements](../topics/requirements-and-hints.md) section.

## FAIR Workflows

> The FAIR principles have laid a foundation for sharing and publishing
> digital assets, and in particular, data. The FAIR principles emphasize
> machine accessibility and that all digital assets should be Findable,
> Accessible, Interoperable, and Reusable. Workflows encode the methods
> by which the scientific process is conducted and via which data are
> created. It is thus important that workflows support the creation
> of FAIR data and adhere to the FAIR principles.
> — [FAIR Computational Workflows](https://workflows.community/groups/fair/),
> Workflows Community Initiative.

CWL has roots in "make" and many similar tools that determine order of
execution, based on dependencies between tasks. However, unlike "make", CWL
tasks are isolated, and you must be explicit about your inputs and outputs.

The benefit of explicitness and isolation are flexibility, portability, and
scalability; tools and workflows described with CWL can transparently leverage
technologies such as Docker and be used with CWL implementations from different
vendors.

`cwltool` also uses the PROV-O standard ontology for data provenance.

## Learn More

- Semantic Versioning - <https://semver.org/>
- The CWL Specification page in the CWL website: <https://www.commonwl.org/specification/>
- The current CWL specification on GitHub: {{ '<https://github.com/common-workflow-language/cwl-{}>'.format(cwl_version_text) }}
- The list of Implementations in the CWL website: <https://www.commonwl.org/implementations/>
- PROV-O: The PROV Ontology - <https://www.w3.org/TR/prov-o/>
- CWL Operations are covered in the [Operations](../topics/operations.md) section of this user guide.
