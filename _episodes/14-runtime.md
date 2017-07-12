---
title: "Creating Files at Runtime"
teaching: 10
exercises: 0
questions:
- "What do I do when I want to create values dynamically and CWL doesn't
provide a built-in way of doing so?"
objectives:
- "Learn how to insert JavaScript expressions into a CWL description."
keypoints:
- "Use `InitialWorkDirRequirement` to specify input files that need to be
created during tool runtime."
---
Sometimes you need to create a file on the fly from input parameters,
such as tools which expect to read their input configuration from a file
rather than the command line parameters.  To do this, use
`InitialWorkDirRequirement`.

*createfile.cwl*

```
{% include cwl/createfile.cwl %}
```

*echo-job.yml*

```
{% include cwl/echo-job.yml %}
```

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

```
$ cwltool createfile.cwl echo-job.yml
[job 140528604979344] /home/example$ cat example.conf
CONFIGVAR=Hello world!
Final process status is success
{}
```
