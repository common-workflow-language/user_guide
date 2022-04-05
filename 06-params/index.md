---
teaching: 10
exercises: 0
questions:
- "How can I re-use parameter values in another location?"
objectives:
- "Learn how to make parameter references in descriptions."
keypoints:
- "Some fields permit parameter references enclosed in `$(...)`."
- "References are written using a subset of Javascript syntax."
---

# Parameter References

In a previous example, we extracted a file using the "tar" program.
However, that example was very limited because it assumed that the file
we were interested in was called "hello.txt", and this was written into the
`.cwl` file. This is not the best way to do this, as the "hello.txt" filename
may vary or be dependant on the input file(s) used.  To avoid this we can
specify the name of the file we want in the job parameters file (`.yml`). In
this example, you will see how to reference the value of input parameters
dynamically from other fields, which will allow us to then specify the name of
the file to extract.

*tar-param.cwl*

```{literalinclude} /_includes/cwl/06-params/tar-param.cwl
:language: yaml
```

*tar-param-job.yml*

```{literalinclude} /_includes/cwl/06-params/tar-param-job.yml
:language: yaml
```

Create your input files and invoke `cwl-runner` with the tool wrapper and the
input object on the command line:

~~~
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
~~~

Certain fields permit parameter references which are enclosed in `$(...)`.
These are evaluated and replaced with value being referenced.

~~~
outputs:
  extracted_out:
    type: File
    outputBinding:
      glob: $(inputs.extractfile)
~~~

References are written using a subset of Javascript syntax.  In this
example, `$(inputs.extractfile)`, `$(inputs["extractfile"])`, and
`$(inputs['extractfile'])` are equivalent.

The value of the "inputs" variable is the input object provided when the
CWL tool was invoked.

Note that because `File` parameters are objects, to get the path to an
input file you must reference the path field on a file object; to
reference the path to the tar file in the above example you would write
`$(inputs.tarfile.path)`.

```{note}
> <p class="rubric">Where are parameter references allowed?</p>
> You can only use parameter references in certain fields.  These are:
>
> - From [`CommandLineTool`](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandLineTool)
>   - `arguments`
>     - `valueFrom`
>   - `stdin`
>   - `stdout`
>   - `stderr`
>   - From [CommandInputParameter](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandInputParameter)
>     - `format`
>     - `secondaryFiles`
>     - From [`inputBinding`](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandLineBinding)
>       - `valueFrom`
>   - From [CommandOutputParamater](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandOutputParameter)
>     - `format`
>     - `secondaryFiles`
>     - From [CommandOutputBinding](http://www.commonwl.org/v1.0/CommandLineTool.html#CommandOutputBinding)
>       - `glob`
>       - `outputEval`
> - From `Workflow`
>   - From [InputParameter](http://www.commonwl.org/v1.0/Workflow.html#InputParameter) and [WorkflowOutputParameter](http://www.commonwl.org/v1.0/Workflow.html#WorkflowOutputParameter)
>     - `format`
>     - `secondaryFiles`
>     - From `steps`
>       - From [WorkflowStepInput](http://www.commonwl.org/v1.0/Workflow.html#WorkflowStepInput)
>         - `valueFrom`
> - From [ExpressionTool](https://www.commonwl.org/v1.0/Workflow.html#ExpressionTool)
>   - `expression`
>   - From [InputParameter](http://www.commonwl.org/v1.0/Workflow.html#InputParameter) and [ExpressionToolOutputParameter](http://www.commonwl.org/v1.0/Workflow.html#ExpressionToolOutputParameter)
>     - `format`
>     - `secondaryFiles`
> - From [`ResourceRequirement`](http://www.commonwl.org/v1.0/CommandLineTool.html#ResourceRequirement)
>   - `coresMin`
>   - `coresMax`
>   - `ramMin`
>   - `ramMax`
>   - `tmpdirMin`
>   - `tmpdirMax`
>   - `outdirMin`
>   - `outdirMax`
> - From [`InitialWorkDirRequirement`](http://www.commonwl.org/v1.0/CommandLineTool.html#InitialWorkDirRequirement)
>   - `listing`
>   - in [Dirent](http://www.commonwl.org/v1.0/CommandLineTool.html#Dirent)
>     - `entry`
>     - `entryname`
> - From `EnvVarRequirement`
>   - From [EnvironmentDef](http://www.commonwl.org/v1.0/CommandLineTool.html#EnvironmentDef)
>     - `envValue`
```

```{include} ../_includes/links.md
```
