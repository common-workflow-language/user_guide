---
teaching: 10
exercises: 0
questions:
- "Where does the output of a command go?"
- "How can I save the output of a command?"
objectives:
- "Learn how to describe and handle outputs from a tool."
keypoints:
- "Outputs are described in the `outputs` section of a CWL description."
- "The field `outputBinding` describes how to to set the value of each
output parameter."
- "Wildcards are allowed in the `glob` field."
---

# Returning Output Files

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

```{note}
> <p class="rubric">Passing mandatory arguments to the `baseCommand`</p>
>
> In previous examples, the `baseCommand` was just a string, with any arguments passed as CWL inputs.
> Instead of a single string we can use an _array of strings_.  The first element is the command to run, and
> any subsequent elements are mandatory command line arguments
```

*tar.cwl*

```{literalinclude} /_includes/cwl/04-output/tar.cwl
:language: yaml
```

*tar-job.yml*

```{literalinclude} /_includes/cwl/04-output/tar-job.yml
:language: yaml
```

Next, create a tar file for the example and invoke `cwl-runner` with the tool
wrapper and the input object on the command line:

~~~
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
~~~

The field `outputBinding` describes how to set the value of each
output parameter.

~~~
outputs:
  example_out:
    type: File
    outputBinding:
      glob: hello.txt
~~~

The `glob` field consists of the name of a file in the output directory.
If you don't know name of the file in advance, you can use a wildcard pattern like `glob: '*.txt'`.

```{include} ../_includes/links.md
```
