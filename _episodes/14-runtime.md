---
title: "Creating Files at Runtime"
teaching: 10
exercises: 0
questions:
- "How do I create required input files from input parameters at runtime?"
objectives:
- "Learn how to create files on the fly during runtime."
keypoints:
- "Use `InitialWorkDirRequirement` to specify input files that need to be
created during tool runtime."
---
Sometimes you need to create a file on the fly from input parameters,
such as tools which expect to read their input configuration from a file
rather than the command line parameters.  To do this, use
`InitialWorkDirRequirement`.

*createfile.cwl*

~~~
{% include cwl/14-runtime/createfile.cwl %}
~~~
{: .source}

*echo-job.yml*

~~~
{% include cwl/14-runtime/echo-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ cwl-runner createfile.cwl echo-job.yml
[job createfile.cwl] /home/example$ cat \
    example.conf > /home/example/output.txt
[job createfile.cwl] completed success
{
    "example_out": {
        "location": "file:///home/example/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$5d3f955d1bb862ec618bc2f7ca4c5fa29fa39e89",
        "size": 22,
        "path": "/home/example/output.txt"
    }
}
Final process status is success
$ cat output.txt
CONFIGVAR=Hello world!
~~~
{: .output}
{% include links.md %}
