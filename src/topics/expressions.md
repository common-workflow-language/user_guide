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
```

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

## Using External Libraries and Inline JavaScript Code with `expressionLib`

The requirement `InlineJavascriptRequirement` supports an `expressionLib` attribute
that allows users to load external JavaScript files, or to provide inline JavaScript
code.

Entries added to the `expressionLib` attribute are parsed with the JavaScript engine
of a CWL runner. This can be used to include external files or to create JavaScript
functions that can be called in other parts of the CWL document.

```{note}

The CWL standards (versions 1.0 through 1.2) [states](https://www.commonwl.org/v1.0/CommandLineTool.html#Expressions)
 that the only version of JavaScript valid in CWL expressions is
[ECMAScript 5.1](https://262.ecma-international.org/5.1/). This means that any
code that you include or write in your CWL Document must be compliant with
ECMAScript 5.1.
```

For example, we can use `InlineJavascriptRequirement` and write a JavaScript function
inline in `expressionLib`. That function can then be used in other parts of the
CWL document:

```{literalinclude} /_includes/cwl/expressions/hello-world-expressionlib-inline.cwl
:language: cwl
:caption: "`hello-world-expressionlib-inline.cwl`"
:name: "`hello-world-expressionlib-inline.cwl`"
:emphasize-lines: 5, 14, 32
```

Running this CWL workflow will invoke the JavaScript function and result in
the `echo` command printing the input message with capital initial letters:

```{runcmd} cwltool hello-world-expressionlib-inline.cwl --message "hello world"
:caption: "Running `hello-world-expressionlib-inline.cwl`."
:name: running-hell-world-expressionlib-inline-cwl
:working-directory: src/_includes/cwl/expressions/
```

Let's move the `capitalizeWords` function to an external file, `custom-functions.js`, and
import it in our CWL document:

```{literalinclude} /_includes/cwl/expressions/custom-functions.js
:language: javascript
:caption: "`custom-functions.js`"
:name: "`custom-functions.js`"
```

```{literalinclude} /_includes/cwl/expressions/hello-world-expressionlib-external.cwl
:language: cwl
:caption: "`hello-world-expressionlib-external.cwl`"
:name: "`hello-world-expressionlib-external.cwl`"
:emphasize-lines: 5-6, 14
```

The `custom-functions.js` file is included in the CWL document with the `$include: custom-functions.js`
statement. That makes the functions and variables available to be used in other parts of
the CWL document.

```{runcmd} cwltool hello-world-expressionlib-external.cwl --message "hello world"
:caption: "Running `hello-world-expressionlib-external.cwl`."
:name: running-hell-world-expressionlib-external-cwl
:working-directory: src/_includes/cwl/expressions/
```

Finally, note that you can have both inline and external JavaScript code in your
CWL document. In this final example we have added another entry to the `expressionLib`
attribute with the new function `createHelloWorldMessage`, that calls the `capitalizeWords`
function from the external file `custom-functions.js`.

```{literalinclude} /_includes/cwl/expressions/hello-world-expressionlib.cwl
:language: cwl
:caption: "`hello-world-expressionlib.cwl`"
:name: "`hello-world-expressionlib.cwl`"
:emphasize-lines: 5-17, 25
```

```{runcmd} cwltool hello-world-expressionlib.cwl --message "hello world"
:caption: "Running `hello-world-expressionlib.cwl`."
:name: running-hell-world-expressionlib-cwl
:working-directory: src/_includes/cwl/expressions/
```

```{note}
The `$include` statement can be used to include a file from the local disk or from a remote location.
It works with both relative and absolute paths. Read the [text about `$include`](https://www.commonwl.org/v1.0/SchemaSalad.html#Include)
from the CWL specification to learn more about it.
```
