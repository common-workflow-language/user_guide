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

digraph G {
    compound=true;
    rankdir="LR";
    fontname="Verdana";
    fontsize="10";
    graph [splines=ortho];

    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];

    subgraph cluster_0 {
      command[style="filled" label=<<FONT FACE='sans-serif;'>echo</FONT>>];
      label="baseCommand";
      fill=gray;
    }

    inputs -> command [lhead=cluster_0];
    command -> outputs [ltail=cluster_0];
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
