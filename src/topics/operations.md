# Operations

An Operation is a type of CWL process, just like a workflow, a command-line tool, or
an expression tool. It is a step of a workflow that specifies inputs and outputs,
but it does not provide enough information to be executed.

You can create operations to visualize a workflow during development, before
you are ready to submit the workflow to a CWL runner:

```{literalinclude} /_includes/cwl/operations/operations.cwl
:language: cwl
:name: operations.cwl
:caption: "`operations.cwl`"
```

The `uppercase` step of the workflow is an operation. It can be used like
a command line tool or an expression. You can also plot it with the
CWL Viewer or `cwltool`:

```{runcmd} cwltool --print-dot operations.cwl
:working-directory: src/_includes/cwl/operations/
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

If you try running it with `cwltool`, the command will fail since `cwltool`
does not have enough information to know how to execute it:

```{runcmd} cwltool operations.cwl --message Hello
:working-directory: src/_includes/cwl/operations/
:name: operations-output-error-cwltool
:caption: "`cwltool` does not know how to run operations"
```

```{note}

CWL runners may come up with ways to bind operations to concrete steps.
A CWL runner could, for instance, use abstract operations with ID's that
correspond to steps executed by a different workflow engine.
```
