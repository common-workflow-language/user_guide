---
orphan: true
---

# Operations

Operation is a type of CWL process just like a workflow, a command line tool, or
an expression tool. It is a step of a workflow that specifies inputs and outputs,
but it does not provide enough information to be executed.

You can create operations to visualize a workflow during development, before
you are ready to submit the workflow to a CWL runner:

```{code-block} cwl
:name: operations.cwl
:caption: "`operations.cwl`"

cwlVersion: v1.2
class: Workflow


inputs:
  message: string
outputs: []

steps:
  echo:
    run: echo.cwl
    in:
      message: message
    out: [out]
  # Here you know you want an operation that changes the case of
  # the previous step, but you do not have an implementation yet.
  uppercase:
    run:
      class: Operation
      inputs:
        message: string
      outputs:
        out: string
    in:
      message:
        source: echo/out
    out: [uppercase_message]
```

The `uppercase` step of the workflow is an operation. It can be used like
use a command line tool or an expression. You can also plot it with the
CWL Viewer or `cwltool`:

```{code-block} console
$ cwltool --print-dot operations.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220628170238
INFO Resolved 'operations.cwl' to 'file:///tmp/operations.cwl'
digraph G {
bgcolor="#eeeeee";
clusterrank=local;
labeljust=right;
labelloc=bottom;
"echo" [fillcolor=lightgoldenrodyellow, label=echo, shape=record, style=filled];
"uppercase" [fillcolor=lightgoldenrodyellow, label=uppercase, shape=record, style=dashed];
"echo" -> "uppercase";
subgraph cluster_inputs {
label="Workflow Inputs";
rank=same;
style=dashed;
"message" [fillcolor="#94DDF4", label=message, shape=record, style=filled];
}

"message" -> "echo";
subgraph cluster_outputs {
label="Workflow Outputs";
labelloc=b;
rank=same;
style=dashed;
}

}
```

The output of the command above can be rendered with a Graphviz renderer. The following
image is rendered with the Sphinx Graphviz directive (this user guide is built with Sphinx):

```{graphviz}

digraph G {
bgcolor="#eeeeee";
clusterrank=local;
labeljust=right;
labelloc=bottom;
"echo" [fillcolor=lightgoldenrodyellow, label=echo, shape=record, style=filled];
"uppercase" [fillcolor=lightgoldenrodyellow, label=uppercase, shape=record, style=dashed];
"echo" -> "uppercase";
subgraph cluster_inputs {
label="Workflow Inputs";
rank=same;
style=dashed;
"message" [fillcolor="#94DDF4", label=message, shape=record, style=filled];
}

"message" -> "echo";
subgraph cluster_outputs {
label="Workflow Outputs";
labelloc=b;
rank=same;
style=dashed;
}

}
```

If you try running it with `cwltool` the command will fail, since `cwltool`
does not have enough information to know how to execute it:

```{code-block} console
:name: operations-output-error-cwltool
:caption: "`cwltool` does not know how to run operations"

$ cwltool operations.cwl --message Hello
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220628170238
INFO Resolved 'operations.cwl' to 'file:///tmp/operations.cwl'
ERROR Workflow error, try again with --debug for more information:
operations.cwl:19:7: Workflow has unrunnable abstract Operation
```

```{note}

CWL runners may come up with ways to bind operations to concrete steps.
A CWL runner could, for instance, use abstract operations with ID's that
correspond to steps executed by a different workflow engine.
```
