---
title: "Returning Output Files"
teaching: 10
exercises: 0
questions:
- "How do I describe outputs from a command?"
objectives:
- "Learn how to describe and handle outputs from a tool."
keypoints:
- "Outputs are described in the `outputs` section of a CWL description."
- "The field `outputBinding` describes how to to set the value of each
output parameter."
- "Wildcards are allowed in the `glob` field."
---
The `outputs` of a tool is a list of output parameters that should be
returned after running the tool.  Each parameter has an `id` for the name
of parameter, and `type` describing what types of values are valid for
that parameter.

When a tool runs under CWL, the starting working directory is the
designated output directory.  The underlying tool or script must record
its results in the form of files created in the output directory.  The
output parameters returned by the CWL tool are either the output files
themselves, or come from examining the content of those files.

*tar.cwl*

~~~
{% include cwl/04-output/tar.cwl %}
~~~
{: .source}

*tar-job.yml*

~~~
{% include cwl/04-output/tar-job.yml %}
~~~
{: .source}

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
        "checksum": "sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "basename": "hello.txt",
        "nameroot": "hello",
        "nameext": ".txt",
        "location": "file:///home/me/cwl/user_guide/hello.txt",
        "path": "/home/me/cwl/user_guide/hello.txt",
        "class": "File",
        "size": 0
    }
}
Final process status is success
~~~
{: .output}

The field `outputBinding` describes how to to set the value of each
output parameter.

~~~
outputs:
  example_out:
    type: File
    outputBinding:
      glob: hello.txt
~~~
{: .source}

The `glob` field consists of the name of a file in the output directory.
If you don't know name of the file in advance, you can use a wildcard pattern like `glob: '*.txt'`.

{% include links.md %}
