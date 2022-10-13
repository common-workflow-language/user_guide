# Parameter References

In a previous example, we extracted a file using the "tar" program.
However, that example was very limited because it assumed that the file
we were interested in was called "hello.txt", and this was written into the
`.cwl` file. This is not the best way to do this, as the "hello.txt" filename
may vary or be dependent on the input file(s) used.  To avoid this we can
specify the name of the file we want in the job parameters file (`.yml`). In
this example, you will see how to reference the value of input parameters
dynamically from other fields, which will allow us to then specify the name of
the file to extract.

```{literalinclude} /_includes/cwl/parameter-references/tar-param.cwl
:language: cwl
:caption: "`tar-param.cwl`"
:name: tar-param.cwl
```

```{literalinclude} /_includes/cwl/parameter-references/tar-param-job.yml
:language: yaml
:caption: "`tar-param-job.yml`"
:name: tar-param-job.yml
```

Create your input files and invoke `cwltool` with the tool description and the
input object on the command line:

```{code-block} console
$ rm hello.tar || true && touch goodbye.txt && tar -cvf hello.tar goodbye.txt
```

```{runcmd} cwltool tar-param.cwl tar-param-job.yml
:working-directory: src/_includes/cwl/parameter-references
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
