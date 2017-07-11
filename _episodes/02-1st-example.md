---
title: "First Example"
teaching: 5
exercises: 5
questions:
- "How do I wrap a simple command line tool?"
objectives:
- "Learn the basic structure of a CWL description."
keypoints:
- "CWL documents are written in YAML and/or JSON."
- "The command called is specified with `baseCommand`."
- "Each expected input is described in the `inputs` section."
- "Input values are specified in a separate YAML file."
- "The tool description and input files are provided as arguments to a CWL runner."
---
The simplest "hello world" program.  This accepts one input parameter, writes a message to the terminal or job log, and produces no permanent output. CWL documents are written in [JSON][json] or [YAML][yaml], or a mix of the two.


*1st-tool.cwl*
{% include: cwl/1st-tool.cwl %}

Use a YAML object in a separate file to describe the input of a run:

*echo-job.yml*
{% include: cwl/echo-job.yml %}

Now invoke `cwl-runner` with the tool wrapper and the input object on the command line:

```
$ cwl-runner 1st-tool.cwl echo-job.yml
[job 140199012414352] $ echo 'Hello world!'
Hello world!
Final process status is success
```

What's going on here?  Let's break it down:

```
cwlVersion: v1.0
class: CommandLineTool
```

The `cwlVersion` field indicates the version of the CWL spec used by the document.  The `class` field indicates this document describes a command line tool.

```
baseCommand: echo
```

The `baseCommand` provides the name of program that will actually run (`echo`)

```
inputs:
  message:
    type: string
      inputBinding:
        position: 1
```

The `inputs` section describes the inputs of the tool.  This is a list of input parameters and each parameter includes an identifier, a data type, and optionally an `inputBinding` which describes how this input parameter should appear on the command line.  In this example, the `position` field indicates where it should appear on the command line.

```
outputs: []
```

This tool has no formal output, so the `outputs` section is an empty list.

[json]: http://json.org
[yaml]: http://yaml.org
