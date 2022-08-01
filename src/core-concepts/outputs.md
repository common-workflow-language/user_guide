# Outputs

## Returning Output Files

The `outputs` of a tool is a list of output parameters that should be
returned after running the tool.  Each parameter has an `id` for the name
of parameter, and `type` describing what types of values are valid for
that parameter.

When a tool runs under CWL, the starting working directory is the
designated output directory.  The underlying tool or script must record
its results in the form of files created in the output directory.  The
output parameters returned by the CWL tool are either the output files
themselves, or come from examining the content of those files.

The following example demonstrates how to return a file that has been extracted from a tar file.

```{tip}
Passing mandatory arguments to the `baseCommand`

In previous examples, the `baseCommand` was just a string, with any arguments passed as CWL inputs.
Instead of a single string we can use an _array of strings_.  The first element is the command to run, and
any subsequent elements are mandatory command line arguments
```

*tar.cwl*

```{literalinclude} /_includes/cwl/04-output/tar.cwl
:language: cwl
```

*tar-job.yml*

```{literalinclude} /_includes/cwl/04-output/tar-job.yml
:language: yaml
```

Next, create a tar file for the example and invoke `cwl-runner` with the tool
wrapper and the input object on the command line:

```bash
$ touch hello.txt && tar -cvf hello.tar hello.txt
$ cwl-runner tar.cwl tar-job.yml
[job tar.cwl] /tmp/tmpqOeawQ$ tar \
    --extract --file \
    /tmp/tmpGDk8Y1/stg80bbad20-494d-47af-8075-dffc32df03a3/hello.tar
[job tar.cwl] completed success
{
    "example_out": {
        "location": "file:///home/me/cwl/user_guide/hello.txt",
        "basename": "hello.txt",
        "class": "File",
        "checksum": "sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "size": 0,
        "path": "/home/me/cwl/user_guide/hello.txt"
    }
}
Final process status is success
```

The field `outputBinding` describes how to set the value of each
output parameter.

```cwl
outputs:
  example_out:
    type: File
    outputBinding:
      glob: hello.txt
```

The `glob` field consists of the name of a file in the output directory.
If you don't know name of the file in advance, you can use a wildcard pattern like `glob: '*.txt'`.

## Capturing Standard Output

To capture a tool's standard output stream, add the `stdout` field with
the name of the file where the output stream should go.  Then add `type:
stdout` on the corresponding output parameter.

*stdout.cwl*

```{literalinclude} /_includes/cwl/05-stdout/stdout.cwl
:language: cwl
```

*echo-job.yml*

```{literalinclude} /_includes/cwl/05-stdout/echo-job.yml
:language: yaml
```

Now invoke `cwl-runner` providing the tool wrapper and the input object
on the command line:

```bash
$ cwl-runner stdout.cwl echo-job.yml
[job stdout.cwl] /tmp/tmpE0gTz7$ echo \
    'Hello world!' > /tmp/tmpE0gTz7/output.txt
[job stdout.cwl] completed success
{
    "example_out": {
        "location": "file:///home/me/cwl/user_guide/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$47a013e660d408619d894b20806b1d5086aab03b",
        "size": 13,
        "path": "/home/me/cwl/user_guide/output.txt"
    }
}
Final process status is success
```

## Parameter References

In a previous example, we extracted a file using the "tar" program.
However, that example was very limited because it assumed that the file
we were interested in was called "hello.txt", and this was written into the
`.cwl` file. This is not the best way to do this, as the "hello.txt" filename
may vary or be dependent on the input file(s) used.  To avoid this we can
specify the name of the file we want in the job parameters file (`.yml`). In
this example, you will see how to reference the value of input parameters
dynamically from other fields, which will allow us to then specify the name of
the file to extract.

*tar-param.cwl*

```{literalinclude} /_includes/cwl/06-params/tar-param.cwl
:language: cwl
```

*tar-param-job.yml*

```{literalinclude} /_includes/cwl/06-params/tar-param-job.yml
:language: yaml
```

Create your input files and invoke `cwl-runner` with the tool wrapper and the
input object on the command line:

```bash
$ rm hello.tar || true && touch goodbye.txt && tar -cvf hello.tar goodbye.txt
$ cwl-runner tar-param.cwl tar-param-job.yml
[job tar-param.cwl] /tmp/tmpwH4ouT$ tar \
    --extract --file \
    /tmp/tmpREYiEt/stgd7764383-99c9-4848-af51-7c2d6e5527d9/hello.tar \
    goodbye.txt
[job tar-param.cwl] completed success
{
    "extracted_file": {
        "location": "file:///home/me/cwl/user_guide/goodbye.txt",
        "basename": "goodbye.txt",
        "class": "File",
        "checksum": "sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "size": 0,
        "path": "/home/me/cwl/user_guide/goodbye.txt"
    }
}
Final process status is success
```

Certain fields permit parameter references which are enclosed in `$(...)`.
These are evaluated and replaced with value being referenced.

```cwl
outputs:
  extracted_out:
    type: File
    outputBinding:
      glob: $(inputs.extractfile)
```

References are written using a subset of Javascript syntax.  In this
example, `$(inputs.extractfile)`, `$(inputs["extractfile"])`, and
`$(inputs['extractfile'])` are equivalent.

The value of the "inputs" variable is the input object provided when the
CWL tool was invoked.

Note that because `File` parameters are objects, to get the path to an
input file you must reference the path field on a file object; to
reference the path to the tar file in the above example you would write
`$(inputs.tarfile.path)`.

```{admonition} Where are parameter references allowed?

You can only use parameter references in certain fields.  These are:

- From [`CommandLineTool`](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandLineTool)
  - `arguments`
    - `valueFrom`
  - `stdin`
  - `stdout`
  - `stderr`
  - From [CommandInputParameter](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandInputParameter)
    - `format`
    - `secondaryFiles`
    - From [`inputBinding`](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandLineBinding)
      - `valueFrom`
  - From [CommandOutputParamater](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandOutputParameter)
    - `format`
    - `secondaryFiles`
    - From [CommandOutputBinding](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandOutputBinding)
      - `glob`
      - `outputEval`
- From `Workflow`
  - From [InputParameter](http://www.commonwl.org/v1.0/Workflow.html#InputParameter) and [WorkflowOutputParameter](http://www.commonwl.org/v1.0/Workflow.html#WorkflowOutputParameter)
    - `format`
    - `secondaryFiles`
    - From `steps`
      - From [WorkflowStepInput](http://www.commonwl.org/v1.0/Workflow.html#WorkflowStepInput)
        - `valueFrom`
- From [ExpressionTool](https://www.commonwl.org/v1.0/Workflow.html#ExpressionTool)
  - `expression`
  - From [InputParameter](http://www.commonwl.org/v1.0/Workflow.html#InputParameter) and [ExpressionToolOutputParameter](http://www.commonwl.org/v1.0/Workflow.html#ExpressionToolOutputParameter)
    - `format`
    - `secondaryFiles`
- From [`ResourceRequirement`](http://www.commonwl.org/v1.0/CommandLineTool.html#ResourceRequirement)
  - `coresMin`
  - `coresMax`
  - `ramMin`
  - `ramMax`
  - `tmpdirMin`
  - `tmpdirMax`
  - `outdirMin`
  - `outdirMax`
- From [`InitialWorkDirRequirement`](http://www.commonwl.org/v1.0/CommandLineTool.html#InitialWorkDirRequirement)
  - `listing`
  - in [Dirent](http://www.commonwl.org/v1.0/CommandLineTool.html#Dirent)
    - `entry`
    - `entryname`
- From `EnvVarRequirement`
  - From [EnvironmentDef](http://www.commonwl.org/v1.0/CommandLineTool.html#EnvironmentDef)
    - `envValue`
```

## Array Outputs

You can also capture multiple output files into an array of files using `glob`.

*array-outputs.cwl*

```{literalinclude} /_includes/cwl/10-array-outputs/array-outputs.cwl
:language: cwl
```

*array-outputs-job.yml*

```{literalinclude} /_includes/cwl/10-array-outputs/array-outputs-job.yml
:language: yaml
```

Now invoke `cwl-runner` providing the tool wrapper and the input object
on the command line:

```bash
$ cwl-runner array-outputs.cwl array-outputs-job.yml
[job 140190876078160] /home/example$ touch foo.txt bar.dat baz.txt
Final process status is success
{
  "output": [
    {
      "size": 0,
      "location": "foo.txt",
      "checksum": "sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709",
      "class": "File"
    },
    {
      "size": 0,
      "location": "baz.txt",
      "checksum": "sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709",
      "class": "File"
    }
  ]
}
```

As described in the [YAML Guide](../yaml/index.md#arrays),
the array of expected outputs is specified in `array-outputs-job.yml` with each
entry marked by a leading `-`. This format can also be used in CWL descriptions
to mark entries in arrays, as demonstrated in several of the upcoming sections.

% TODO
%
% - Creating files at runtime - https://github.com/common-workflow-language/user_guide/issues/134
