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

```{literalinclude} /_includes/cwl/04-output/tar.cwl
:language: cwl
:caption: "`tar.cwl`"
:name: tar.cwl
```

```{literalinclude} /_includes/cwl/04-output/tar-job.yml
:language: yaml
:caption: "`tar-job.yml`"
:name: tar-job.yml
```

Next, create a tar file for the example.

```{code-block} console
$ touch hello.txt && tar -cvf hello.tar hello.txt
hello.txt
```

And now invoke `cwl-runner` with the tool wrapper and the input object on the command line:

```{code-block} console
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

```{literalinclude} /_includes/cwl/05-stdout/stdout.cwl
:language: cwl
:caption: "`stdout.cwl`"
:name: stdout.cwl
```

```{literalinclude} /_includes/cwl/05-stdout/echo-job.yml
:language: yaml
:caption: "`echo-job.yml`"
```

Now invoke `cwl-runner` providing the tool wrapper and the input object
on the command line:

```{code-block} console
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

## Array Outputs

You can also capture multiple output files into an array of files using `glob`.

```{literalinclude} /_includes/cwl/10-array-outputs/array-outputs.cwl
:language: cwl
:caption: "`array-outputs.cwl`"
:name: array-outputs.cwl
```

```{literalinclude} /_includes/cwl/10-array-outputs/array-outputs-job.yml
:language: yaml
:caption: "`array-outputs-job.yml`"
:name: array-outputs-job.yml
```

Now invoke `cwl-runner` providing the tool wrapper and the input object
on the command line:

```{code-block} console
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

As described in the [YAML Guide](yaml-guide.md#arrays),
the array of expected outputs is specified in `array-outputs-job.yml` with each
entry marked by a leading `-`. This format can also be used in CWL descriptions
to mark entries in arrays, as demonstrated in several of the upcoming sections.

% TODO
%
% - Creating files at runtime - https://github.com/common-workflow-language/user_guide/issues/134
