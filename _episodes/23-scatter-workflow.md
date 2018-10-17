---
title: "Scattering Workflows"
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
- Scatter runs on each step specified independently
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
{% include cwl/23-scatter-workflow/scatter-job.yml %}
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
`message_array`. Ok, so how about if we want to scatter over two steps in a workflow?

Let's perform a simple echo like above, but capturing `stdout` by adding the following 
lines instead of `outputs: []`

*1st-tool-mod.cwl*

~~~
outputs:
  echo_out:
    type: stdout
~~~

And add a second step that uses `wc` to count the characters in each file. See the tool
below:

*wc-tool.cwl*

~~~
{% include cwl/23-scatter-workflow/wc-tool.cwl %}
~~~

Now, how do we incorporate scatter? Remember the scatter field is under each step:

~~~
{% include cwl/23-scatter-workflow/scatter-two-steps.cwl %}
~~~

Here we have placed the scatter field under each step. This is fine for this example since
it runs quickly, but if you're runnung many samples for a more complex workflow, you may 
wish to consider an alternative. Here we are running scatter on each step independently, but
since the second step is not dependent on the first step completing all languages, we aren't
using the scatter functionality efficiently. The second step expects an array as input from 
the first step, so it will wait until everything in step one is finished before doing anything.
Pretend that `echo Hello World!` takes 1 minute to perform, `wc -c` on the output takes 3 minutes 
and that `echo Hallo welt!` takes 5 minutes to perform, and `wc` on that output takes 3 minutes. 
Even though `echo Hello World!` could finish in 4 minutes, it will actually finish in 8 minutes 
because the first step must wait on `echo Hallo welt!`. You can see how this might not scale
well. 

Ok, so how do we scatter on steps that can proceed independent of other samples? Remember from
chapter 22, that we can make an entire workflow a single step in another workflow! Convert our
two step workflow to a single step subworkflow:

*scatter-nested-workflow.cwl*

~~~
{% include cwl/23-scatter-workflow/scatter-nested-workflow.cwl %}
~~~

Now the scatter acts on a single step, but that step consists of two steps so each step is performed
in parallel.


