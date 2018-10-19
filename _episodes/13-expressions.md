---
title: "JavaScript Expressions"
teaching: 10
exercises: 0
questions:
- "What do I do when I want to create values dynamically and CWL doesn't
provide a built-in way of doing so?"
objectives:
- "Learn how to insert JavaScript expressions into a CWL description."
keypoints:
- "If `InlineJavascriptRequirement` is specified, you can include JavaScript
expressions that will be evaluated by the CWL runner."
- "Expressions are only valid in certain fields."
- "Expressions should only be used when no built in CWL solution exists."
---
If you need to manipulate input parameters, include the requirement
`InlineJavascriptRequirement` and then anywhere a parameter reference is
legal you can provide a fragment of Javascript that will be evaluated by
the CWL runner.

__Note: JavaScript expressions should only be used when absolutely necessary.
When manipulating file names, extensions, paths etc, consider whether one of the
[built in `File` properties][file-prop] like `basename`, `nameroot`, `nameext`,
etc, could be used instead.
See the [list of recommended practices][rec-practices].__

*expression.cwl*

~~~
{% include cwl/13-expressions/expression.cwl %}
~~~
{: .source}

As this tool does not require any `inputs` we can run it with an (almost) empty
job file:

*empty.yml*

~~~
{% include cwl/13-expressions/empty.yml %}
~~~
{: .source}

`empty.yml` contains a description of an empty JSON object. JSON objects
descriptions are contained inside curly brackets `{}`, so an empty object is
represented simply by a set of empty brackets.

We can then run `expression.cwl`:

~~~
$ cwl-runner expression.cwl empty.yml
[job expression.cwl] /home/example$ echo \
    -A \
    2 \
    -B \
    baz \
    -C \
    10 \
    9 \
    8 \
    7 \
    6 \
    5 \
    4 \
    3 \
    2 \
    1 > /home/example/output.txt
[job expression.cwl] completed success
{
    "example_out": {
        "location": "file:///home/example/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$a739a6ff72d660d32111265e508ed2fc91f01a7c",
        "size": 36,
        "path": "/home/example/output.txt"
    }
}
Final process status is success
$ cat output.txt
-A 2 -B baz -C 10 9 8 7 6 5 4 3 2 1
~~~
{: .output}

Note that requirements must be provided as an array, with each entry (in this
case, only `class: InlineJavascriptRequirement`) marked by a `-`. The same
syntax is used to describe the additional command line arguments.

> ## Where are JavaScript expressions allowed?
> Just like [parameter references]({{ page.root }}{% link _episodes/06-params.md %}), you can use JavaScript Expressions
> only in certain fields.  These are:
> 
> - From [`CommandLineTool`](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandLineTool)
>   - `arguments`
>     - `valueFrom`
>   - `stdin`
>   - `stdout`
>   - `stderr`
>   - From [CommandInputParameter](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandInputParameter)
>     - `format`
>     - `secondaryFiles`
>     - From [`inputBinding`](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandLineBinding)
>       - `valueFrom`
>   - From [CommandOutputParamater](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandOutputParameter)
>     - `format`
>     - `secondaryFiles`
>     - From [CommandOutputBinding](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandOutputBinding)
>       - `glob`
>       - `outputEval`
> - From `Workflow`
>   - From [InputParameter](https://www.commonwl.org/v1.0/Workflow.html#InputParameter) and [WorkflowOutputParameter](https://www.commonwl.org/v1.0/Workflow.html#WorkflowOutputParameter)
>     - `format`
>     - `secondaryFiles`
>     - From `steps`
>       - From [WorkflowStepInput](https://www.commonwl.org/v1.0/Workflow.html#WorkflowStepInput)
>         - `valueFrom`
> - From [ExpressionTool](https://www.commonwl.org/v1.0/Workflow.html#ExpressionTool)
>   - `expression`
>   - From [InputParameter](https://www.commonwl.org/v1.0/Workflow.html#InputParameter) and [ExpressionToolOutputParameter](https://www.commonwl.org/v1.0/Workflow.html#ExpressionToolOutputParameter)
>     - `format`
>     - `secondaryFiles`
> - From [`ResourceRequirement`](https://www.commonwl.org/v1.0/CommandLineTool.html#ResourceRequirement)
>   - `coresMin`
>   - `coresMax`
>   - `ramMin`
>   - `ramMax`
>   - `tmpdirMin`
>   - `tmpdirMax`
>   - `outdirMin`
>   - `outdirMax`
> - From [`InitialWorkDirRequirement`](https://www.commonwl.org/v1.0/CommandLineTool.html#InitialWorkDirRequirement)
>   - `listing`
>   - in [Dirent](https://www.commonwl.org/v1.0/CommandLineTool.html#Dirent)
>     - `entry`
>     - `entryname`
> - From `EnvVarRequirement`
>   - From [EnvironmentDef](https://www.commonwl.org/v1.0/CommandLineTool.html#EnvironmentDef)
>     - `envValue`
{: .callout }


[file-prop]: https://www.commonwl.org/v1.0/CommandLineTool.html#File
[rec-practices]: https://www.commonwl.org/user_guide/rec-practices/
{% include links.md %}
