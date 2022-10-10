# Additional Arguments and Parameters

Sometimes tools require additional command line options that don't
correspond exactly to input parameters.

In this example, we will wrap the Java compiler to compile a java source
file to a class file.  By default, "javac" will create the class files in
the same directory as the source file.  However, CWL input files (and the
directories in which they appear) may be read-only, so we need to
instruct "javac" to write the class file to the designated output directory
instead.

```{literalinclude} /_includes/cwl/additional-arguments-and-parameters/arguments.cwl
:language: cwl
:caption: "`arguments.cwl`"
:name: arguments.cwl
```

```{literalinclude} /_includes/cwl/additional-arguments-and-parameters/arguments-job.yml
:language: yaml
:caption: "`arguments-job.yml`"
```

Next, create a sample Java file to use with the command-line tool.

```{code-block} console
$ echo "public class Hello {}" > Hello.java
```

And now invoke `cwltool` providing the tool description and the input object on the command line:

```{runcmd} cwltool arguments.cwl arguments-job.yml
:working-directory: src/_includes/cwl/additional-arguments-and-parameters
```

Here we use the `arguments` field to add an additional argument to the
command line that isn't tied to a specific input parameter.

```cwl
arguments: ["-d", $(runtime.outdir)]
```

This example references a runtime parameter.  Runtime parameters provide
information about the hardware or software environment when the tool is
actually executed.  The `$(runtime.outdir)` parameter is the path to the
designated output directory.  Other parameters include `$(runtime.tmpdir)`,
`$(runtime.ram)`, `$(runtime.cores)`, `$(runtime.outdirSize)`, and
`$(runtime.tmpdirSize)`.  See the [Runtime Environment][runtime] section of the
CWL specification for details.

[runtime]: https://www.commonwl.org/v1.0/CommandLineTool.html#Runtime_environment
