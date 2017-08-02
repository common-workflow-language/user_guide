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
{% include cwl/createfile.cwl %}
~~~
{: .source}

*echo-job.yml*

~~~
{% include cwl/echo-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ cwltool createfile.cwl echo-job.yml
[job 140528604979344] /home/example$ cat example.conf
CONFIGVAR=Hello world!
Final process status is success
{}
~~~
{: .output}
