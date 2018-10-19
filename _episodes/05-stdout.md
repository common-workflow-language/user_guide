---
title: "Capturing Standard Output"
teaching: 10
exercises: 0
questions:
- "How do I capture a tool's standard output stream?"
objectives:
- "Learn how to capture streamed output from a tool."
keypoints:
- "Use the `stdout` field to specify a filename to capture streamed output."
- "The corresponding output parameter must have `type: stdout`."
---
To capture a tool's standard output stream, add the `stdout` field with
the name of the file where the output stream should go.  Then add `type:
stdout` on the corresponding output parameter.

*stdout.cwl*

~~~
{% include cwl/05-stdout/stdout.cwl %}
~~~
{: .source}

*echo-job.yml*

~~~
{% include cwl/05-stdout/echo-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` providing the tool wrapper and the input object
on the command line:

~~~
$ cwl-runner stdout.cwl echo-job.yml
[job stdout.cwl] /tmp/tmpE0gTz7$ echo \
    'Hello world!' > /tmp/tmpE0gTz7/output.txt
[job stdout.cwl] completed success
{
    "example_out": {
        "checksum": "sha1$47a013e660d408619d894b20806b1d5086aab03b",
        "basename": "output.txt",
        "nameroot": "output",
        "nameext": ".txt",
        "location": "file:///home/me/cwl/user_guide/output.txt",
        "path": "/home/me/cwl/user_guide/output.txt",
        "class": "File",
        "size": 13
    }
}
Final process status is success

~~~
{: .output}
{% include links.md %}
