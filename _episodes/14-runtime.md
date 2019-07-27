---
title: "Creating Files at Runtime"
teaching: 10
exercises: 0
questions:
- "How do I create required input files from input parameters at runtime?"
- "How do I invoke a script rather than just a simple command line?"
- "How do I pass arguments to my script?"
objectives:
- "Learn how to create files on the fly during runtime."
- "Learn how to use expressions in bash scripts."
keypoints:
- "Use `InitialWorkDirRequirement` to specify input files that need to be
created during tool runtime."
---
Sometimes you need to create a file on the fly from input parameters,
such as tools which expect to read their input configuration from a file
rather than the command line parameters, or need a small wrapper shell script.

To generate such files we can use the `InitialWorkDirRequirement`.

*createfile.cwl*

~~~
{% include cwl/14-runtime/createfile.cwl %}
~~~
{: .source}

Any [expressions](../13-expressions/index.html) like `$(inputs.message)` are expanded by the CWL engine before creating the file; here inserting the value at the input `message`.

> **Tip:** The _CWL expressions_ are independent of any _shell variables_ used later during command line tool invocation. That means that any genuine need for the character `$` should be **escaped** with `\`, for instance `\${PREFIX}` above is expanded to `${PREFIX}` in the generated file to be evaluated by the shell script instead of the CWL engine.

To test the above CWL tool use this job to provide the input value `message`:

*echo-job.yml*

~~~
{% include cwl/14-runtime/echo-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ cwl-runner createfile.cwl echo-job.yml
[job createfile.cwl] /private/tmp/docker_tmphrqxxcdl$ sh \
    example.sh > /private/tmp/docker_tmphrqxxcdl/output.txt
Could not collect memory usage, job ended before monitoring began.
[job createfile.cwl] completed success
{
    "example_out": {
        "location": "file:///home/example/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$9045abe4bd04dd8ccfe50c6ff61820b784b64aa7",
        "size": 25,
        "path": "/home/example/output.txt"
    }
}
Final process status is success
$ cat output.txt
Message is: Hello world!
~~~
{: .output}



{% include links.md %}
