A workflow is a CWL processing unit that executes command-line tools,
expression tools, or workflows (sub-workflows) as steps. It must have
`inputs`, `outputs`, and `steps` defined in the CWL document.

```{graphviz}
:name: workflow-graph
:caption: CWL workflow.
:align: center

digraph G {
    compound=true;
    rankdir="LR";
    fontname="Verdana";
    fontsize="10";
    graph [splines=ortho];

    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];

    subgraph cluster_0 {
      node [width = 1.75];
      steps_0[style="filled" label="Command-line tools"];
      steps_1[style="filled" label="Expression tools"];
      steps_2[style="filled" label="Sub-workflows"];
      label="steps";
      fill=gray;
    }

    inputs -> steps_1 [lhead=cluster_0];
    steps_1 -> outputs [ltail=cluster_0];
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
