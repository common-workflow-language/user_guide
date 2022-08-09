# Creating files at runtime

Sometimes you need to create a file on the fly from input parameters,
such as tools which expect to read their input configuration from a file
rather than the command line parameters, or need a small wrapper shell script.

To generate such files we can use the `InitialWorkDirRequirement`.

```{literalinclude} /_includes/cwl/14-runtime/createfile.cwl
:language: cwl
:caption: "`createfile.cwl`"
:name: createfile.cwl
```

Any [expressions](../essential-topics/expressions.md) like `$(inputs.message)` are
expanded by the CWL engine before creating the file;
here inserting the value at the input `message`.

```{tip}
The _CWL expressions_ are independent of any _shell variables_
used later during command line tool invocation. That means that any genuine
need for the character `$` must be **escaped** with `\`,
for instance `\${PREFIX}` above is expanded to `${PREFIX}` in the generated file
to be evaluated by the shell script instead of the CWL engine.
```

To test the above CWL tool use this job to provide the input value `message`:

```{literalinclude} /_includes/cwl/14-runtime/echo-job.yml
:language: yaml
:caption: "`echo-job.yml`"
:name: echo-job.yml
```

Before we run this, lets look at each step in a little more detail.
The base command `baseCommand: ["sh", "example.sh"]`
will execute the command `sh example.sh`.
This will run the file we create in the shell.

`InitialWorkDirRequirement` requires a `listing`.
As the `listing` is a YAML array we need a `-` on the first line of
each element of the array, in this case we have just one element.
`entryname:` can have any value,
but it must match what was specified in the `baseCommand`.
The final part is `entry:`, this is followed by `|-`
which is YAML quoting syntax, and means that you are using a multiline string
(without it, we would need to write the whole script on one line).

```{note}

See the [YAML Guide](../yaml/index.md#maps) for more about the formatting.
```

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

```{code-block} console
$ cwl-runner createfile.cwl echo-job.yml
[job createfile.cwl] /private/tmp/docker_tmphrqxxcdl$ sh \
    example.sh > /private/tmp/docker_tmphrqxxcdl/output.txt
Could not collect memory usage, job ended before monitoring began.
[job createfile.cwl] completed success
{
    "example_out": {
        "location": "file:///home/example/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$9045abe4bd04dd8ccfe50c6ff61820b784b64aa7",
        "size": 25,
        "path": "/home/example/output.txt"
    }
}
Final process status is success
$ cat output.txt
Message is: Hello world!
```
