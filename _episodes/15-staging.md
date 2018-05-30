---
title: "Staging Input Files"
teaching: 10
exercises: 0
questions:
- "How do I stage input files in the working directory?"
objectives:
- "Learn how to handle situations where a tool expects to write output files to
the same directory as its input files."
keypoints:
- "Input files are normally kept in a read-only directory."
- "Use `InitialWorkDirRequirement` to stage input files in the working
directory."
---
Normally, input files are located in a read-only directory separate from
the output directory.  This causes problems if the underlying tool expects to
write its output files alongside the input file in the same directory.  You use `InitialWorkDirRequirement` to stage input files into the output directory.
In this example, we use a JavaScript expression to extract the base name of the
input file from its leading directory path.

*linkfile.cwl*

~~~
{% include cwl/15-staging/linkfile.cwl %}
~~~
{: .source}

*arguments-job.yml*

~~~
{% include cwl/15-staging/arguments-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ cwl-runner linkfile.cwl arguments-job.yml
[job 139928309171664] /home/example$ docker run -i --volume=/home/example/Hello.java:/var/lib/cwl/job557617295_examples/Hello.java:ro --volume=/home/example:/var/spool/cwl:rw --volume=/tmp/tmpmNbApw:/tmp:rw --workdir=/var/spool/cwl --read-only=true --net=none --user=1001 --rm --env=TMPDIR=/tmp java:7 javac Hello.java
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
{: .output}
{% include links.md %}
