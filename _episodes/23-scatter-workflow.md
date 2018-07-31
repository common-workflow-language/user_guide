---
title: "Scatter Workflows"
teaching: 10
exercises: 0
questions:
- "How do I run tools or workflows in parallel?"
objectives:
- "Learn how to create workflows that can run a step over a list of inputs."
keypoints:
- "A workflow can scatter over an input array in a step of a workflow, if the workflow engine
supports the `ScatterFeatureRequirement`."
- The `scatter` field is specified for each step you want to scatter
- The `scatter` field references the step level inputs, not the workflow inputs
---
Now that we know how to write workflows, we can start utilizing the `ScatterFeatureRequirement`.
This feature tells the runner that you wish to run a tool or workflow multiple times over a list
of inputs. The workflow then takes the input(s) as an array and will run the specified step(s) 
on each element of the array as if it were a single input. This allows you to run the same workflow
on multiple inputs without having to generate many different commands or input yaml files.

~~~
requirements:
  - class: ScatterFeatureRequirement
~~~
{: .source}

The most common reason a new user might want to use scatter is to perform the same analysis on 
different samples. Let's start with a simple workflow that calls our first example and takes 
an array of strings as input to the workflow:

*scatter-workflow.cwl*

~~~
{% include cwl/23-scatter-workflow/scatter-workflow.cwl %}
~~~
{: .source}

Aside from the `requirements` section including `ScatterFeatureRequirement`, what is
going on here?

~~~
inputs:
  message_array: string[] 
~~~

First of all, notice that the workflow level input here accepts an array of strings.

~~~
steps:
  echo:
    run: 1st-tool.cwl
    scatter: message
    in:
      message: message_array
    out: []
~~~

Here we've added a new field to the step `echo` called `scatter`. This field tells the
runner that we'd like to scatter over this input for this particular step. Note that
the input listed after scatter is the step's input, not the workflow input. 

For our first scatter, it's as simple as that! Since our tool doesn't collect any outputs, we
still use `outputs: []` in our workflow, but if you expect that the final output of your 
workflow will now have multiple outputs to collect, be sure to update that to an array type
as well!

Using the following input file:

*scatter-job.yml*

~~~
{% include cwl/23-scatter-workflow/scatter-job.cwl %}
~~~
{: .source}

As a reminder, `1st-tool.cwl` simply calls the command `echo` on a message. If we invoke
`cwl-runner scatter-workflow.cwl scatter-job.yml` on the command line:

~~~
$ cwl-runner scatter-workflow.cwl scatter-job.yml 
[workflow scatter-workflow.cwl] start
[step echo] start
[job echo] /tmp/tmp0hqmg400$ echo \
    'Hello world!'
Hello world!
[job echo] completed success
[step echo] start
[job echo_2] /tmp/tmpu65_m1zw$ echo \
    'Hola mundo!'
Hola mundo!
[job echo_2] completed success
[step echo] start
[job echo_3] /tmp/tmp5cs7a2wh$ echo \
    'Bonjour le monde!'
Bonjour le monde!
[job echo_3] completed success
[step echo] start
[job echo_4] /tmp/tmp301wo7p8$ echo \
    'Hallo welt!'
Hallo welt!
[job echo_4] completed success
[step echo] completed success
[workflow scatter-workflow.cwl] completed success
{}
Final process status is success
~~~ 

You can see that the workflow calls echo multiple times on each element of our 
`message_array`. 
