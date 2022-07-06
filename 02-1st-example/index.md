---
teaching: 5
exercises: 0
questions:
- "How do I write a CWL description of a simple command line tool?"
objectives:
- "Learn the basic structure of a CWL description."
keypoints:
- "CWL documents are written in YAML and/or JSON."
- "The command called is specified with `baseCommand`."
- "Each expected input is described in the `inputs` section."
- "Input values are specified in a separate YAML file."
- "The tool description and input files are provided as arguments to a CWL runner."
---

# First Example

The simplest "hello world" program.  This accepts one input parameter, writes a message to the terminal or job log, and produces
no permanent output.
CWL documents are written in [JSON][json] or [YAML][yaml], or a mix of the two.
We will use YAML throughout this guide.
If you are not familiar with YAML,
you may find it helpful to refer to
[this quick tutorial for the subset of YAML used in CWL](/yaml/index.md).

First, create a file called `1st-tool.cwl`, containing the boxed text below. It will help you to use a text editor that can be
specified to produce text in YAML or JSON. Whatever text editor you use, the indents you see should not be created using tabs.

*1st-tool.cwl*

```{literalinclude} /_includes/cwl/02-1st-example/1st-tool.cwl
:language: cwl
```

Next, create a file called `echo-job.yml`, containing the following boxed text, which will describe the input of a run:

*echo-job.yml*

```{literalinclude} /_includes/cwl/02-1st-example/echo-job.yml
:language: yaml
```

Now, invoke `cwl-runner` with the tool wrapper `1st-tool.cwl` and the input object echo-job.yml on the command line. The command
is  `cwl-runner 1st-tool.cwl echo-job.yml`. The boxed text below shows this command and the expected output.

```bash
$ cwl-runner 1st-tool.cwl echo-job.yml
[job 1st-tool.cwl] /tmp/tmpmM5S_1$ echo \
    'Hello world!'
Hello world!
[job 1st-tool.cwl] completed success
{}
Final process status is success

```

The command `cwl-runner 1st-tool.cwl echo-job.yml` is an example of a general form that you will often come across while using
CWL. The general form is `cwl-runner [tool-or-workflow-description] [input-job-settings]`

What's going on here?  Let's break down the contents of `1st-tool.cwl`:

```cwl
cwlVersion: v1.0
class: CommandLineTool
```

The `cwlVersion` field indicates the version of the CWL spec used by the document.  The `class` field indicates this document
describes a command line tool.

```cwl
baseCommand: echo
```

The `baseCommand` provides the name of program that will actually run (`echo`). `echo` is a built-in program in the bash and
C shells.

```yaml
inputs:
  message:
    type: string
    inputBinding:
      position: 1
```

The `inputs` section describes the inputs of the tool.
This is a mapped list of input parameters
(see the [YAML Guide](/yaml/index.md) for more about the format)
and each parameter includes an identifier,
a data type,
and optionally an `inputBinding`.
The `inputBinding` describes how this input parameter should appear
on the command line.
In this example,
the `position` field indicates where it should appear on the command line.

```cwl
outputs: []
```

This tool has no formal output, so the `outputs` section is an empty list.

[echo]: http://www.linfo.org/echo.html
[json]: http://json.org/
[yaml]: http://yaml.org/
