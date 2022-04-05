---
teaching: 10
exercises: 0
questions:
- "How do I specify arguments that don't require input values?"
- "How do I refer to runtime parameters?"
objectives:
- "Learn how to add additional options to a command."
- "Learn how to reference runtime parameters."
keypoints:
- "Use the `arguments` section to describe command line options that do not
correspond exactly to input parameters."
- "Runtime parameters provide information about the environment when the tool
is actually executed."
- "Runtime parameters are referred under the `runtime` namespace."
---

# Additional Arguments and Parameters

Sometimes tools require additional command line options that don't
correspond exactly to input parameters.

In this example, we will wrap the Java compiler to compile a java source
file to a class file.  By default, "javac" will create the class files in
the same directory as the source file.  However, CWL input files (and the
directories in which they appear) may be read-only, so we need to
instruct "javac" to write the class file to the designated output directory
instead.

*arguments.cwl*

```{literalinclude} /_includes/cwl/08-arguments/arguments.cwl
:language: yaml
```


*arguments-job.yml*

```{literalinclude} /_includes/cwl/08-arguments/arguments-job.yml
:language: yaml
```

Now create a sample Java file and invoke `cwl-runner` providing the tool wrapper
and the input object on the command line:

~~~
$ echo "public class Hello {}" > Hello.java
$ cwl-runner arguments.cwl arguments-job.yml
[job arguments.cwl] /tmp/tmpwYALo1$ docker \
 run \
 -i \
 --volume=/home/peter/work/common-workflow-language/v1.0/examples/Hello.java:/var/lib/cwl/stg8939ac04-7443-4990-a518-1855b2322141/Hello.java:ro \
 --volume=/tmp/tmpwYALo1:/var/spool/cwl:rw \
 --volume=/tmp/tmpptIAJ8:/tmp:rw \
 --workdir=/var/spool/cwl \
 --read-only=true \
 --user=1001 \
 --rm \
 --env=TMPDIR=/tmp \
 --env=HOME=/var/spool/cwl \
 openjdk:9.0.1-11-slim \
 javac \
 -d \
 /var/spool/cwl \
 /var/lib/cwl/stg8939ac04-7443-4990-a518-1855b2322141/Hello.java
Final process status is success
{
  "classfile": {
    "size": 416,
    "location": "/home/example/Hello.class",
    "checksum": "sha1$2f7ac33c1f3aac3f1fec7b936b6562422c85b38a",
    "class": "File"
  }
}

~~~

Here we use the `arguments` field to add an additional argument to the
command line that isn't tied to a specific input parameter.

~~~
arguments: ["-d", $(runtime.outdir)]
~~~

This example references a runtime parameter.  Runtime parameters provide
information about the hardware or software environment when the tool is
actually executed.  The `$(runtime.outdir)` parameter is the path to the
designated output directory.  Other parameters include `$(runtime.tmpdir)`,
`$(runtime.ram)`, `$(runtime.cores)`, `$(runtime.outdirSize)`, and
`$(runtime.tmpdirSize)`.  See the [Runtime Environment][runtime] section of the
CWL specification for details.

[runtime]: https://www.commonwl.org/v1.0/CommandLineTool.html#Runtime_environment
```{include} ../_includes/links.md
```
