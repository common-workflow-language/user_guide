---
title: "Environment Variables"
teaching: 10
exercises: 0
questions:
- "How do I set the value of environment variables for a tool's execution?"
objectives:
- "Learn how to pass environment variables to a tool's runtime."
keypoints:
- "Tools run in a restricted environment with a minimal set of environment
variables."
- "Use the `EnvVarRequirement` field to set environment variables inside a
tool's environment."
---
Tools run in a restricted environment and do not inherit most environment
variables from the parent process.  You can set environment variables for
the tool using `EnvVarRequirement`.

*env.cwl*

~~~
{% include cwl/12-env/env.cwl %}
~~~
{: .source}

*echo-job.yml*

~~~
{% include cwl/12-env/echo-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ cwl-runner env.cwl echo-job.yml
[job env.cwl] /home/example$ env > /home/example/output.txt
[job env.cwl] completed success
{
    "example_out": {
        "location": "file:///home/example/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$1ca16a840b14807b2fd3323022c476b06a150e2f",
        "size": 94,
        "path": "/home/example/output.txt"
    }
}
Final process status is success
$ cat output.txt
HELLO=Hello world!
PATH=/bin:/usr/bin:/usr/local/bin
HOME=/home/example
TMPDIR=/tmp/tmp63Obpk
~~~
{: .output}
{% include links.md %}
