# Expressions

If you need to manipulate input parameters, include the requirement
`InlineJavascriptRequirement` and then anywhere a parameter reference is
legal you can provide a fragment of Javascript that will be evaluated by
the CWL runner.

```{important}
JavaScript expressions should only be used when absolutely necessary.
When manipulating file names, extensions, paths etc, consider whether one of the
[built in `File` properties][file-prop] like `basename`, `nameroot`, `nameext`,
etc, could be used instead.
See the [list of best practices](best-practices.md).

```{literalinclude} /_includes/cwl/expressions/expression.cwl
:language: cwl
:caption: "`expression.cwl`"
:name: expression.cwl
```

As this tool does not require any `inputs` we can run it with an (almost) empty
job file:

```{literalinclude} /_includes/cwl/expressions/empty.yml
:language: yaml
:caption: "`empty.yml`"
:name: empty.cwl
```

`empty.yml` contains a description of an empty JSON object. JSON objects
descriptions are contained inside curly brackets `{}`, so an empty object is
represented simply by a set of empty brackets.

We can then run `expression.cwl`:

```{runcmd} cwltool expression.cwl empty.yml
:name: running-expression.cwl
:caption: Running `expression.cwl`
:working-directory: src/_includes/cwl/expressions/
```

```{runcmd} cat output.txt
:working-directory: src/_includes/cwl/expressions/
```

Note that requirements can be provided with the map syntax, as in the example above:

```cwl
requirements:
  InlineJavascriptRequirement: {}
```

Or as an array, with each entry (in this case, only `class: InlineJavascriptRequirement`) marked by a `-`.
The same syntax is used to describe the additional command line arguments.

```cwl
requirements:
  - class: InlineJavascriptRequirement
```

```{admonition} Where are JavaScript expressions allowed?

Just like [parameter references](parameter-references.md), you can use JavaScript Expressions
only in certain fields.  These are:
- From [`CommandLineTool`](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandLineTool)
  - `arguments`
    - `valueFrom`
  - `stdin`
  - `stdout`
  - `stderr`
  - From [CommandInputParameter](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandInputParameter)
    - `format`
    - `secondaryFiles`
    - From [`inputBinding`](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandLineBinding)
      - `valueFrom`
  - From [CommandOutputParamater](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandOutputParameter)
    - `format`
    - `secondaryFiles`
    - From [CommandOutputBinding](https://www.commonwl.org/v1.0/CommandLineTool.html#CommandOutputBinding)
      - `glob`
      - `outputEval`
- From `Workflow`
  - From [InputParameter](https://www.commonwl.org/v1.0/Workflow.html#InputParameter) and [WorkflowOutputParameter](https://www.commonwl.org/v1.0/Workflow.html#WorkflowOutputParameter)
    - `format`
    - `secondaryFiles`
  - From `steps`
    - From [WorkflowStepInput](https://www.commonwl.org/v1.0/Workflow.html#WorkflowStepInput)
      - `valueFrom`
- From [ExpressionTool](https://www.commonwl.org/v1.0/Workflow.html#ExpressionTool)
  - `expression`
  - From [InputParameter](https://www.commonwl.org/v1.0/Workflow.html#InputParameter) and [ExpressionToolOutputParameter](https://www.commonwl.org/v1.0/Workflow.html#ExpressionToolOutputParameter)
    - `format`
    - `secondaryFiles`
- From [`ResourceRequirement`](https://www.commonwl.org/v1.0/CommandLineTool.html#ResourceRequirement)
  - `coresMin`
  - `coresMax`
  - `ramMin`
  - `ramMax`
  - `tmpdirMin`
  - `tmpdirMax`
  - `outdirMin`
  - `outdirMax`
- From [`InitialWorkDirRequirement`](https://www.commonwl.org/v1.0/CommandLineTool.html#InitialWorkDirRequirement)
  - `listing`
  - in [Dirent](https://www.commonwl.org/v1.0/CommandLineTool.html#Dirent)
    - `entry`
    - `entryname`
- From `EnvVarRequirement`
  - From [EnvironmentDef](https://www.commonwl.org/v1.0/CommandLineTool.html#EnvironmentDef)
    - `envValue`
```

[file-prop]: https://www.commonwl.org/v1.0/CommandLineTool.html#File


% TODO
% - (maybe not before other concepts? move this to after inputs/outputs/etc?)
% - External libraries and expressionLib - https://github.com/common-workflow-language/user_guide/issues/126
