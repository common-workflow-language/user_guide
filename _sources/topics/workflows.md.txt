# Workflows

A workflow is a CWL processing unit that executes command-line tools,
expression tools, or workflows (sub-workflows) as steps. It must have
`inputs`, `outputs`, and `steps` defined in the CWL document.

% TODO: Fix the missing link the graph below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: workflow-graph

```{graphviz}
:caption: CWL workflow.
:align: center

digraph G {
    compound=true;
    rankdir="LR";
    fontname="Verdana";
    fontsize="10";
    graph [splines=ortho];

    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];

    subgraph cluster_0 {
      node [width = 1.75];
      steps_0[style="filled" label="Command-line tools"];
      steps_1[style="filled" label="Expression tools"];
      steps_2[style="filled" label="Sub-workflows"];
      label="steps";
      fill=gray;
    }

    inputs -> steps_1 [lhead=cluster_0];
    steps_1 -> outputs [ltail=cluster_0];
}
```

The CWL document `echo-uppercase.cwl` defines a workflow that runs
the command-line tool, and the expression tool showed in the earlier
examples.

% TODO: Fix the missing link the code below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: echo-uppercase.cwl

```{code-block} cwl
:caption: "`echo-uppercase.cwl`"
cwlVersion: v1.2
class: Workflow

requirements:
  InlineJavascriptRequirement: {}

inputs:
  message: string

outputs:
  out:
    type: string
    outputSource: uppercase/uppercase_message

steps:
  echo:
    run: echo.cwl
    in:
      message: message
    out: [out]
  uppercase:
    run: uppercase.cwl
    in:
      message:
        source: echo/out
    out: [uppercase_message]
```

A command-line tool or expression tool can also be written directly
in the same CWL document as the workflow. For example, we can rewrite
the `echo-uppercase.cwl` workflow as a single file:

% TODO: Fix the missing link the code below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: echo-uppercase-single-file.cwl

```{code-block} cwl
:caption: "`echo-uppercase-single-file.cwl`"
cwlVersion: v1.2
class: Workflow

requirements:
  InlineJavascriptRequirement: {}

inputs:
  message: string

outputs:
  out:
    type: string
    outputSource: uppercase/uppercase_message

steps:
  echo:
    run:
      class: CommandLineTool

      baseCommand: echo

      stdout: output.txt

      inputs:
        message:
          type: string
          inputBinding: {}
      outputs:
        out:
          type: string
          outputBinding:
            glob: output.txt
            loadContents: true
            outputEval: $(self[0].contents)
    in:
      message: message
    out: [out]
  uppercase:
    run:
      class: ExpressionTool

      requirements:
        InlineJavascriptRequirement: {}

      inputs:
        message: string
      outputs:
        uppercase_message: string

      expression: |
        ${ return {"uppercase_message": inputs.message.toUpperCase()}; }
    in:
      message:
        source: echo/out
    out: [uppercase_message]
```

Having separate files helps with modularity and code organization. But
it can be helpful writing everything in a single file for development.
There are other ways to combine multiple files into a single file
(e.g. `cwltool --pack`) discussed further in other sections of this
user guide.

% TODO: add a link to the page about SubworkflowFeatureRequirement

```{note}

For a sub-workflows you need to enable the requirement
`SubworkflowFeatureRequirement`. It is covered in another section
of this user guide in more detail.
```

## Writing Workflows

This workflow extracts a java source file from a tar file and then
compiles it.

```{literalinclude} /_includes/cwl/workflows/1st-workflow.cwl
:language: cwl
:caption: "`1st-workflow.cwl`"
:name: 1st-workflow.cwl
```

% TODO: The link below is for a previous commit with the workflow above. Ideally, I think we should either use `cwltool`
%       or Python to add the graph here. Or, maybe re-create the graph for the latest main version?

```{admonition} Visualization of 1st-workflow.cwl
[![Visualization of 1st-workflow.cwl](https://view.commonwl.org/graph/png/github.com/common-workflow-language/user_guide/blob/a29e7eae0006660946fc705a310b37a21a7e1edc/_includes/cwl/21-1st-workflow/1st-workflow.cwl)](https://view.commonwl.org/graph/png/github.com/common-workflow-language/user_guide/blob/a29e7eae0006660946fc705a310b37a21a7e1edc/_includes/cwl/21-1st-workflow/1st-workflow.cwl)
```

Use a YAML or a JSON object in a separate file to describe the input of a run:

```{literalinclude} /_includes/cwl/workflows/1st-workflow-job.yml
:language: yaml
:caption: "`1st-workflow-job.yml`"
:name: 1st-workflow-job.yml
```

Next, create a sample Java file and add it to a tar file to use with the command-line tool.

```{code-block} console
$ echo "public class Hello {}" > Hello.java && tar -cvf hello.tar Hello.java
Hello.java
```

Now invoke `cwltool` with the tool description and the input object on the
command line:

```{runcmd} cwltool 1st-workflow.cwl 1st-workflow-job.yml
:working-directory: src/_includes/cwl/workflows/
```

What's going on here?  Let's break it down:

```cwl
cwlVersion: v1.0
class: Workflow
```

The `cwlVersion` field indicates the version of the CWL spec used by the
document.  The `class` field indicates this document describes a workflow.

```cwl
inputs:
  tarball: File
  name_of_file_to_extract: string
```

The `inputs` section describes the inputs of the workflow.  This is a
list of input parameters where each parameter consists of an identifier
and a data type.  These parameters can be used as sources for input to
specific workflows steps.

```cwl
outputs:
  compiled_class:
    type: File
    outputSource: compile/classfile
```

The `outputs` section describes the outputs of the workflow.  This is a
list of output parameters where each parameter consists of an identifier
and a data type.  The `outputSource` connects the output parameter `classfile`
of the `compile` step to the workflow output parameter `compiled_class`.

```cwl
steps:
  untar:
    run: tar-param.cwl
    in:
      tarfile: tarball
      extractfile: name_of_file_to_extract
    out: [extracted_file]
```

The `steps` section describes the actual steps of the workflow.  In this
example, the first step extracts a file from a tar file, and the second
step compiles the file from the first step using the java compiler.
Workflow steps are not necessarily run in the order they are listed,
instead the order is determined by the dependencies between steps (using
`source`).  In addition, workflow steps which do not depend on one
another may run in parallel.

The first step, `untar` runs `tar-param.cwl` (described previously in
[Parameter References](parameter-references.md)).
This tool has two input parameters, `tarfile` and `extractfile` and one output
parameter `extracted_file`.

The ``in`` section of the workflow step connects these two input parameters to
the inputs of the workflow, `tarball` and `name_of_file_to_extract` using
`source`.  This means that when the workflow step is executed, the values
assigned to `tarball` and `name_of_file_to_extract` will be used for the
parameters `tarfile` and `extractfile` in order to run the tool.

The `out` section of the workflow step lists the output parameters that are
expected from the tool.

```cwl
  compile:
    run: arguments.cwl
    in:
      src: untar/extracted_file
    out: [classfile]
```

The second step `compile` depends on the results from the first step by
connecting the input parameter `src` to the output parameter of `untar` using
`untar/extracted_file`.  It runs `arguments.cwl` (described previously in
[Additional Arguments and Parameters](additional-arguments-and-parameters.md)).
The output of this step `classfile` is connected to the
`outputs` section for the Workflow, described above.

## Nested Workflows

Workflows are ways to combine multiple tools to perform a larger operations.
We can also think of a workflow as being a tool itself; a CWL workflow can be
used as a step in another CWL workflow, if the workflow engine supports the
`SubworkflowFeatureRequirement`:

```cwl
requirements:
  SubworkflowFeatureRequirement: {}
```

Here's an example workflow that uses our `1st-workflow.cwl` as a nested
workflow:

```{literalinclude} /_includes/cwl/workflows/nestedworkflows.cwl
:language: cwl
:caption: "`nestedworkflows.cwl`"
:name: nestedworkflows.cwl
```

```{note}
<p class="rubric">Visualization of the workflow and the inner workflow from its `compile` step</a>

This two-step workflow starts with the `create-tar` step which is connected to
the `compile` step in orange; `compile` is another workflow, diagrammed on the
right. In purple we see the fixed string `"Hello.java"` being supplied as the
`name_of_file_to_extract`.

<a href="https://view.commonwl.org/workflows/github.com/common-workflow-language/user_guide/blob/main/_includes/cwl/workflows/nestedworkflows.cwl"><img
src="https://view.commonwl.org/graph/svg/github.com/common-workflow-language/user_guide/blob/main/_includes/cwl/workflows/nestedworkflows.cwl"
alt="Visualization of nestedworkflows.cwl" /></a>
<a href="https://view.commonwl.org/workflows/github.com/common-workflow-language/user_guide/blob/main/_includes/cwl/workflows/1st-workflow.cwl"><img
src="https://view.commonwl.org/graph/svg/github.com/common-workflow-language/user_guide/blob/main/_includes/cwl/workflows/1st-workflow.cwl"
alt="Visualization of 1st-workflow.cwl" /></a>
```

A CWL `Workflow` can be used as a `step` just like a `CommandLineTool`, its CWL
file is included with `run`. The workflow inputs (`tarball` and `name_of_file_to_extract`) and outputs
(`compiled_class`) then can be mapped to become the step's input/outputs.

```cwl
  compile:
    run: 1st-workflow.cwl
    in:
      tarball: create-tar/tar_compressed_java_file
      name_of_file_to_extract:
        default: "Hello.java"
    out: [compiled_class]
```

Our `1st-workflow.cwl` was parameterized with workflow inputs, so when running
it we had to provide a job file to denote the tar file and `*.java` filename.
This is generally best-practice, as it means it can be reused in multiple parent
workflows, or even in multiple steps within the same workflow.

Here we use `default:` to hard-code `"Hello.java"` as the `name_of_file_to_extract`
input, however our workflow also requires a tar file at `tarball`, which we will
prepare in the `create-tar` step. At this point it is probably a good idea to refactor
`1st-workflow.cwl` to have more specific input/output names, as those also
appear in its usage as a tool.

It is also possible to do a less generic approach and avoid external
dependencies in the job file. So in this workflow we can generate a hard-coded
`Hello.java` file using the previously mentioned `InitialWorkDirRequirement`
requirement, before adding it to a tar file.

```cwl
  create-tar:
    requirements:
      InitialWorkDirRequirement:
        listing:
          - entryname: Hello.java
            entry: |
              public class Hello {
                public static void main(String[] argv) {
                    System.out.println("Hello from Java");
                }
              }
```

In this case our step can assume `Hello.java` rather than be parameterized, so
we can use hardcoded values `hello.tar` and `Hello.java` in a `baseCommand` and
the resulting `outputs`:

```cwl
  run:
    class: CommandLineTool
    inputs: []
    baseCommand: [tar, --create, --file=hello.tar, Hello.java]
    outputs:
      tar_compressed_java_file:
        type: File
        streamable: true
        outputBinding:
          glob: "hello.tar"
```

Did you notice that we didn't split out the `tar --create` tool to a separate file,
but rather embedded it within the CWL Workflow file? This is generally not best
practice, as the tool then can't be reused. The reason for doing it in this case
is because the command line is hard-coded with filenames that only make sense
within this workflow.

In this example we had to prepare a tar file outside, but only because our inner
workflow was designed to take that as an input. A better refactoring of the
inner workflow would be to take a list of Java files to compile, which would
simplify its usage as a tool step in other workflows.

Nested workflows can be a powerful feature to generate higher-level functional
and reusable workflow units - but just like for creating a CWL Tool description,
care must be taken to improve its usability in multiple workflows.

## Scattering Steps

Now that we know how to write workflows, we can start utilizing the `ScatterFeatureRequirement`.
This feature tells the runner that you wish to run a tool or workflow multiple times over a list
of inputs. The workflow then takes the input(s) as an array and will run the specified step(s)
on each element of the array as if it were a single input. This allows you to run the same workflow
on multiple inputs without having to generate many different commands or input yaml files.

```cwl
requirements:
  ScatterFeatureRequirement: {}
```

The most common reason a new user might want to use scatter is to perform the same analysis on
different samples. Let's start with a simple workflow that calls our first example
(`hello_world.cwl`) and takes an array of strings as input to the workflow:

```{literalinclude} /_includes/cwl/workflows/scatter-workflow.cwl
:language: cwl
:caption: "`scatter-workflow.cwl`"
:name: scatter-workflow.cwl
```

Aside from the `requirements` section including `ScatterFeatureRequirement`, what is
going on here?

```cwl
inputs:
  message_array: string[]
```

First of all, notice that the main workflow level input here requires an array of strings.

```cwl
steps:
  echo:
    run: hello_world.cwl
    scatter: message
    in:
      message: message_array
    out: []
```

Here we've added a new field to the step `echo` called `scatter`. This field tells the
runner that we'd like to scatter over this input for this particular step. Note that
the input name listed after scatter is the one of the step's input, not a workflow level input.

For our first scatter, it's as simple as that! Since our tool doesn't collect any outputs, we
still use `outputs: []` in our workflow, but if you expect that the final output of your
workflow will now have multiple outputs to collect, be sure to update that to an array type
as well!

Using the following input file:

```{literalinclude} /_includes/cwl/workflows/scatter-job.yml
:language: yaml
:caption: "`scatter-job.yml`"
:name: scatter-job.yml
```

As a reminder, [`hello_world.cwl`](../introduction/quick-start.md) simply calls the command
`echo` on a message. If we invoke `cwltool scatter-workflow.cwl scatter-job.yml` on the
command line:

```{runcmd} cwltool scatter-workflow.cwl scatter-job.yml
:working-directory: src/_includes/cwl/workflows/
```

You can see that the workflow calls echo multiple times on each element of our
`message_array`. Ok, so how about if we want to scatter over two steps in a workflow?

Let's perform a simple echo like above, but capturing `stdout` by adding the following
lines instead of `outputs: []`

```{code-block} cwl
:caption: "`hello_world_to_stdout.cwl`"
:name: hello_world_to_stdout.cwl
outputs:
  echo_out:
    type: stdout
```

And add a second step that uses `wc` to count the characters in each file. See the tool
below:

```{literalinclude} /_includes/cwl/workflows/wc-tool.cwl
:language: cwl
:caption: "`wc-tool.cwl`"
:name: wc-tool.cwl
```

Now, how do we incorporate scatter? Remember the scatter field is under each step:

```{literalinclude} /_includes/cwl/workflows/scatter-two-steps.cwl
:language: cwl
:caption: "`scatter-two-steps.cwl`"
:name: scatter-two-steps.cwl
```

Here we have placed the scatter field under each step. This is fine for this example since
it runs quickly, but if you're running many samples for a more complex workflow, you may
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
[Nested Workflows](#nested-workflows), that we can make an entire workflow a single step in another workflow! Convert our
two-step workflow to a single step subworkflow:

```{literalinclude} /_includes/cwl/workflows/scatter-nested-workflow.cwl
:language: cwl
:caption: "`scatter-nested-workflow.cwl`"
:name: scatter-nested-workflow.cwl
```

Now the scatter acts on a single step, but that step consists of two steps so each step is performed
in parallel.

## Conditional workflows

This workflow contains a conditional step and is executed based on the input.
This allows workflows to skip additional steps based on input parameters given at the start of the program or by previous steps.

```{code-block} cwl
:caption: "`conditional-workflow.cwl`"
:name: conditional-workflow.cwl
class: Workflow
cwlVersion: v1.2
inputs:
  val: int

steps:

  step1:
    in:
      in1: val
      a_new_var: val
    run: foo.cwl
    when: $(inputs.in1 < 1)
    out: [out1]

  step2:
    in:
      in1: val
      a_new_var: val
    run: foo.cwl
    when: $(inputs.a_new_var > 2)
    out: [out1]

outputs:
  out1:
    type: string
    outputSource:
      - step1/out1
      - step2/out1
    pickValue: first_non_null

requirements:
  InlineJavascriptRequirement: {}
  MultipleInputFeatureRequirement: {}
```

The first thing you'll notice is that this workflow is only compatible for version 1.2 or greater of the CWL standards.

```cwl
class: Workflow
cwlVersion: v1.2
```

The first step of the workflow (step1) contains two input properties and will execute foo.cwl when the conditions are met. The new property `when` is where the condition validation takes place. In this case only when `in1`  from the workflow contains a value `< 1` this step will be executed.

```cwl
steps:

  step1:
    in:
      in1: val
      a_new_var: val
    run: foo.cwl
    when: $(inputs.in1 < 1)
    out: [out1]
```

Using the following command `cwltool cond-wf-003.1.cwl --val 0` the value will pass the first conditional step and will therefore be executed and is shown in the log by `INFO [step step1] start` whereas the second step is skipped as indicated by `INFO [step step2] will be skipped`.

```{code-block} console
INFO [workflow ] start
INFO [workflow ] starting step step1
INFO [step step1] start
INFO [job step1] /private/tmp/docker_tmpdcyoto2d$ echo

INFO [job step1] completed success
INFO [step step1] completed success
INFO [workflow ] starting step step2
INFO [step step2] will be skipped
INFO [step step2] completed skipped
INFO [workflow ] completed success
{
    "out1": "foo 0"
}
INFO Final process status is success
```

When a value of 3 is given the first conditional step will not be executed but the second step will `cwltool cond-wf-003.1.cwl --val 3`.

```{code-block} console
INFO [workflow ] start
INFO [workflow ] starting step step1
INFO [step step1] will be skipped
INFO [step step1] completed skipped
INFO [workflow ] starting step step2
INFO [step step2] start
INFO [job step2] /private/tmp/docker_tmpqwr93mxx$ echo

INFO [job step2] completed success
INFO [step step2] completed success
INFO [workflow ] completed success
{
    "out1": "foo 3"
}
INFO Final process status is success
```

If no conditions are met for example when using `--val 2` the workflow will raise a permanentFail.

```{code-block} console
$ cwltool cond-wf-003.1.cwl --val 2

INFO [workflow ] start
INFO [workflow ] starting step step1
INFO [step step1] will be skipped
INFO [step step1] completed skipped
INFO [workflow ] starting step step2
INFO [step step2] will be skipped
INFO [step step2] completed skipped
ERROR [workflow ] Cannot collect workflow output: All sources for 'out1' are null
INFO [workflow ] completed permanentFail
WARNING Final process status is permanentFail
```

% TODO
% - Scatter
%   - ScatterMethod https://github.com/common-workflow-language/user_guide/issues/29
%   - Also in the **episode 23** of the current User Guide - https://www.commonwl.org/user_guide/workflows/index.html
% - Subworkflows/nested workflows
%   - Covered in the **episode 22** from the current User Guide -  https://www.commonwl.org/user_guide/workflows/index.html
% - Conditionals https://github.com/common-workflow-language/user_guide/issues/191 & https://github.com/common-workflow-language/user_guide/issues/188
%   - Also in the **episode 24** of the current User Guide - https://www.commonwl.org/user_guide/24_conditional-workflow/index.html
