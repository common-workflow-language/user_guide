---
teaching: 24
exercises: 0
questions:
- "How do you write workflows with conditions?"
objectives:
- "Learn how to construct workflows containing conditional steps."
keypoints:
- ""
---

# Conditional workflows

This workflow contains a conditional step and is executed based on the input.
This allows workflows to skip additional steps based on input parameters given at the start of the program or by previous steps.

*conditional-workflow.cwl*

```
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

```
class: Workflow
cwlVersion: v1.2
```

The first step of the worklfow (step1) contains two input properties and will execute foo.cwl when the conditions are met. The new property `when` is where the condition validation takes place. In this case only when `in1`  from the workflow contains a value `< 1` this step will be executed.

```
steps:

  step1:
    in:
      in1: val
      a_new_var: val
    run: foo.cwl
    when: $(inputs.in1 < 1)
    out: [out1]
```

Using the following command `cwltool cond-wf-003.1.cwl --val 0` the value will pass the first conditional step and will therefor be executed and is shown in the log by `INFO [step step1] start` whereas the second step is skipped as indicated by `INFO [step step2] will be skipped`.

```
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

```
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

```
cwltool cond-wf-003.1.cwl --val 2

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

```{include} ../_includes/links.md
```
