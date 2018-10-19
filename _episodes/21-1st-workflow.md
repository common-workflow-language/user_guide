---
title: "Writing Workflows"
teaching: 10
exercises: 0
questions:
- "How do I connect tools together into a workflow?"
objectives:
- "Learn how to construct workflows from multiple CWL tool descriptions."
keypoints:
- "Each step in a workflow must have its own CWL description."
- "Top level inputs and outputs of the workflow are described in the `inputs`
and `outputs` fields respectively."
- "The steps are specified under `steps`."
- "Execution order is determined by the connections between steps."
---
This workflow extracts a java source file from a tar file and then
compiles it.

*1st-workflow.cwl*

~~~
{% include cwl/21-1st-workflow/1st-workflow.cwl %}
~~~
{: .source}

> ## Visualization of 1st-workflow.cwl
> <a href="https://view.commonwl.org/workflows/github.com/common-workflow-language/user_guide/blob/gh-pages/_includes/cwl/21-1st-workflow/1st-workflow.cwl"><img src="https://view.commonwl.org/graph/svg/github.com/common-workflow-language/user_guide/blob/gh-pages/_includes/cwl/21-1st-workflow/1st-workflow.cwl" alt="Visualization of 1st-workflow.cwl" /></a>
{: .callout}

Use a JSON object in a separate file to describe the input of a run:

*1st-workflow-job.yml*

~~~
{% include cwl/21-1st-workflow/1st-workflow-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ echo "public class Hello {}" > Hello.java && tar -cvf hello.tar Hello.java
$ cwl-runner 1st-workflow.cwl 1st-workflow-job.yml
[job untar] /tmp/tmp94qFiM$ tar --create --file /home/example/hello.tar Hello.java
[step untar] completion status is success
[job compile] /tmp/tmpu1iaKL$ docker run -i --volume=/tmp/tmp94qFiM/Hello.java:/var/lib/cwl/job301600808_tmp94qFiM/Hello.java:ro --volume=/tmp/tmpu1iaKL:/var/spool/cwl:rw --volume=/tmp/tmpfZnNdR:/tmp:rw --workdir=/var/spool/cwl --read-only=true --net=none --user=1001 --rm --env=TMPDIR=/tmp java:7 javac -d /var/spool/cwl /var/lib/cwl/job301600808_tmp94qFiM/Hello.java
[step compile] completion status is success
[workflow 1st-workflow.cwl] outdir is /home/example
Final process status is success
{
  "compiled_class": {
    "location": "/home/example/Hello.class",
    "checksum": "sha1$e68df795c0686e9aa1a1195536bd900f5f417b18",
    "class": "File",
    "size": 416
  }
}
~~~
{: .output}

What's going on here?  Let's break it down:

~~~
cwlVersion: v1.0
class: Workflow
~~~
{: .source}

The `cwlVersion` field indicates the version of the CWL spec used by the
document.  The `class` field indicates this document describes a workflow.


~~~
inputs:
  tarball: File
  name_of_file_to_extract: string
~~~
{: .source}

The `inputs` section describes the inputs of the workflow.  This is a
list of input parameters where each parameter consists of an identifier
and a data type.  These parameters can be used as sources for input to
specific workflows steps.

~~~
outputs:
  compiled_class:
    type: File
    outputSource: compile/classfile
~~~
{: .source}

The `outputs` section describes the outputs of the workflow.  This is a
list of output parameters where each parameter consists of an identifier
and a data type.  The `outputSource` connects the output parameter `classfile`
of the `compile` step to the workflow output parameter `compiled_class`.

~~~
steps:
  untar:
    run: tar-param.cwl
    in:
      tarfile: tarball
      extractfile: name_of_file_to_extract
    out: [extracted_file]
~~~
{: .source}

The `steps` section describes the actual steps of the workflow.  In this
example, the first step extracts a file from a tar file, and the second
step compiles the file from the first step using the java compiler.
Workflow steps are not necessarily run in the order they are listed,
instead the order is determined by the dependencies between steps (using
`source`).  In addition, workflow steps which do not depend on one
another may run in parallel.

The first step, `untar` runs `tar-param.cwl` (described previously in
[Parameter references]({{ page.root }}{% link _episodes/06-params.md %})).
This tool has two input parameters, `tarfile` and `extractfile` and one output
parameter `example_out`.

The ``in`` section of the workflow step connects these two input parameters to
the inputs of the workflow, `tarball` and `name_of_file_to_extract` using
`source`.  This means that when the workflow step is executed, the values
assigned to `tarball` and `name_of_file_to_extract` will be used for the
parameters `tarfile` and `extractfile` in order to run the tool.

The `out` section of the workflow step lists the output parameters that are
expected from the tool.

~~~
  compile:
    run: arguments.cwl
    in:
      src: untar/extracted_file
    out: [classfile]
~~~
{: .source}

The second step `compile` depends on the results from the first step by
connecting the input parameter `src` to the output parameter of `untar` using
`untar/extracted_file`.  The output of this step `classfile` is connected to the
`outputs` section for the Workflow, described above.

{% include links.md %}
