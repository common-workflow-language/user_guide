---
teaching: 10
exercises: 0
questions:
- "What can I do if a tool needs to be able to write output to the location where its input files are stored?"
objectives:
- "Learn how to handle situations where a tool expects to write output files to
the same directory as its input files."
keypoints:
- "Input files are normally kept in a read-only directory."
- "Use `InitialWorkDirRequirement` to stage input files in the working
directory."
---

# Staging Input Files

Normally, input files are located in a read-only directory separate from
the output directory.  This causes problems if the underlying tool expects to
write its output files alongside the input file in the same directory.  You use `InitialWorkDirRequirement` to stage input files into the output directory.
In this example, we use a JavaScript expression to extract the base name of the
input file from its leading directory path.

*linkfile.cwl*

```{literalinclude} /_includes/cwl/15-staging/linkfile.cwl
:language: yaml
```

*arguments-job.yml*

```{literalinclude} /_includes/cwl/15-staging/arguments-job.yml
:language: yaml
```

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ cwl-runner linkfile.cwl arguments-job.yml
[job 139928309171664] /home/example$ docker run -i --volume=/home/example/Hello.java:/var/lib/cwl/job557617295_examples/Hello.java:ro --volume=/home/example:/var/spool/cwl:rw --volume=/tmp/tmpmNbApw:/tmp:rw --workdir=/var/spool/cwl --read-only=true --net=none --user=1001 --rm --env=TMPDIR=/tmp openjdk:9.0.1-11-slim javac Hello.java
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
```{include} ../_includes/links.md
```
