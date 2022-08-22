# Expression Tool

An expression tool is a type of Process that can be run by itself or
as a Workflow step. It executes a pure JavaScript expression. It is
meant to be used as a way to isolate complex JavaScript expressions
that need to operate on input data and produce some result as output.

Similar to the command-line tool it requires `inputs` and `outputs`.
But instead of `baseCommand`, it requires an `expression` attribute.

% TODO: Fix the missing link the graph below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: expression-tool-graph

```{graphviz}
:caption: CWL expression tool.
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
      expression[style="filled" label="JavaScript"];
      label="expression";
      fill=gray;
    }

    inputs -> expression [lhead=cluster_0];
    expression -> outputs [ltail=cluster_0];
}
```

% TODO: Fix the missing link the code below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: uppercase.cwl

```{code-block} cwl
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

% TODO:
%
% - Explain better with more examples.
