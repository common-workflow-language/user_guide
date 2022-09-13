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

```{literalinclude} /_includes/cwl/outputs/tar.cwl
:language: cwl
:caption: "`tar.cwl`"
:name: tar.cwl
```

```{literalinclude} /_includes/cwl/outputs/tar-job.yml
:language: yaml
:caption: "`tar-job.yml`"
:name: tar-job.yml
```

Next, create a tar file for the example.

```{code-block} console
$ touch hello.txt && tar -cvf hello.tar hello.txt
hello.txt
```

And now invoke `cwltool` with the tool description and the input object on the command line:

```{runcmd} cwltool tar.cwl tar-job.yml
:working-directory: src/_includes/cwl/outputs/
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

```{literalinclude} /_includes/cwl/outputs/stdout.cwl
:language: cwl
:caption: "`stdout.cwl`"
:name: stdout.cwl
```

```{literalinclude} /_includes/cwl/outputs/echo-job.yml
:language: yaml
:caption: "`echo-job.yml`"
```

Now invoke `cwltool` providing the tool description and the input object
on the command line:

```{runcmd} cwltool stdout.cwl echo-job.yml
:working-directory: src/_includes/cwl/outputs/
```

## Array Outputs

You can also capture multiple output files into an array of files using `glob`.

```{literalinclude} /_includes/cwl/outputs/array-outputs.cwl
:language: cwl
:caption: "`array-outputs.cwl`"
:name: array-outputs.cwl
```

```{literalinclude} /_includes/cwl/outputs/array-outputs-job.yml
:language: yaml
:caption: "`array-outputs-job.yml`"
:name: array-outputs-job.yml
```

Now invoke `cwltool` providing the tool description and the input object
on the command line:

```{runcmd} cwltool array-outputs.cwl array-outputs-job.yml
:working-directory: src/_includes/cwl/outputs/
```

As described in the [YAML Guide](yaml-guide.md#arrays),
the array of expected outputs is specified in `array-outputs-job.yml` with each
entry marked by a leading `-`. This format can also be used in CWL descriptions
to mark entries in arrays, as demonstrated in several of the upcoming sections.

% TODO
%
% - Creating files at runtime - https://github.com/common-workflow-language/user_guide/issues/134
