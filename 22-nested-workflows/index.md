---
teaching: 10
exercises: 0
questions:
- "How do I connect multiple workflows together?"
objectives:
- "Learn how to construct nested workflows from multiple CWL workflow
descriptions."
keypoints:
- "A workflow can be used as a step in another workflow, if the workflow engine
supports the `SubworkflowFeatureRequirement`."
- "The workflows are specified under `steps`, with the worklow's description
file provided as the value to the `run` field."
- "Use `default` to specify a default value for a field, which can be
overwritten by a value in the input object."
- "Use `>` to ignore newlines in long commands split over multiple lines."
---

# Nested Workflows

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

*nestedworkflows.cwl*

```{literalinclude} /_includes/cwl/22-nested-workflows/nestedworkflows.cwl
:language: cwl
```

```{note}
<p class="rubric">Visualization of the workflow and the inner workflow from its `compile` step</a>

This two-step workflow starts with the `create-tar` step which is connected to
the `compile` step in orange; `compile` is another workflow, diagrammed on the
right. In purple we see the fixed string `"Hello.java"` being supplied as the
`name_of_file_to_extract`.

<a href="https://view.commonwl.org/workflows/github.com/common-workflow-language/user_guide/blob/gh-pages/_includes/cwl/22-nested-workflows/nestedworkflows.cwl"><img
src="https://view.commonwl.org/graph/svg/github.com/common-workflow-language/user_guide/blob/gh-pages/_includes/cwl/22-nested-workflows/nestedworkflows.cwl"
alt="Visualization of nestedworkflows.cwl" /></a>
<a href="https://view.commonwl.org/workflows/github.com/common-workflow-language/user_guide/blob/gh-pages/_includes/cwl/22-nested-workflows/1st-workflow.cwl"><img
src="https://view.commonwl.org/graph/svg/github.com/common-workflow-language/user_guide/blob/gh-pages/_includes/cwl/22-nested-workflows/1st-workflow.cwl"
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
