# Creating files at runtime

Sometimes you need to create a file on the fly from input parameters,
such as tools which expect to read their input configuration from a file
rather than the command line parameters, or need a small wrapper shell script.

To generate such files we can use the `InitialWorkDirRequirement`.

```{literalinclude} /_includes/cwl/creating-files-at-runtime/createfile.cwl
:language: cwl
:caption: "`createfile.cwl`"
:name: createfile.cwl
```

Any [expressions](../topics/expressions.md) like `$(inputs.message)` are
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

```{literalinclude} /_includes/cwl/creating-files-at-runtime/echo-job.yml
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

See the [YAML Guide](../topics/yaml-guide.md#maps) for more about the formatting.
```

Now invoke `cwltool` with the tool description and the input object on the
command line:

```{runcmd} cwltool createfile.cwl echo-job.yml
:working-directory: src/_includes/cwl/creating-files-at-runtime/
```

```{runcmd} cat output.txt
:working-directory: src/_includes/cwl/creating-files-at-runtime/
```
