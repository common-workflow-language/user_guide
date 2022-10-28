# Command Line Tool

A command-line tool is a type of Process object that can be run by
itself or as a Workflow step. It is a wrapper for a command like
`ls`, `echo`, `tar`, etc. The command-line tool is defined in the
`baseCommand` attribute of the command-line tool CWL document.

A CWL command-line tool must also have `inputs` and `outputs`.
The following example contains a minimal example of a CWL
command-line tool for the `echo` Linux command, using inputs and
outputs.

% TODO: Fix the missing link the graph below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: command-line-tool-graph

```{graphviz}
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

% TODO: Fix the missing link the code below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: echo.cwl

```{literalinclude} /_includes/cwl/echo.cwl
:language: cwl
:caption: "`echo.cwl`"
```

```{note}

The example above uses a simplified form to define inputs and outputs.
You will learn more about in the [Inputs](../topics/inputs.md)
and in the [Outputs](../topics/outputs.md) sections.
```

% TODO
%
% - Spaces in commands https://github.com/common-workflow-language/user_guide/issues/39
% - Arguments (tell the reader the different use cases for arguments and inputs, tell them there is a section about inputs)


## Network Access
This indicates whether a process requires outgoing IPv4/IPv6 network access.
If a command-line tool is written manually in CWL v1.1+, there is a need to 
specify when network access is required.

```cwl
cwlVersion: v1.2
class: CommandLineTool

requirements:
  NetworkAccess:
     networkAccess: true
```

```{note}
CWL v1.0 command-line tools that are upgraded to v1.1 
or v1.2 get Network Access automatically.
```
