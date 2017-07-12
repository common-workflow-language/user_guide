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
- "The corresponding output parameter must have `type: stdout`"
---
To capture a tool's standard output stream, add the `stdout` field with
the name of the file where the output stream should go.  Then add `type:
stdout` on the corresponding output parameter.

*stdout.cwl*

```
{% include cwl/stdout.cwl %}
```

*echo-job.yml*

```
{% include cwl/echo-job.yml %}
```

Now invoke `cwl-runner` providing the tool wrapper and the input object
on the command line:

```
$ cwl-runner stdout.cwl echo-job.yml
[job 140199012414352] $ echo 'Hello world!' > output.txt
Final process status is success
{
"output": {
  "location": "output.txt",
  "size": 13,
  "class": "File",
  "checksum": "sha1$47a013e660d408619d894b20806b1d5086aab03b"
  }
}
$ cat output.txt
Hello world!
```
