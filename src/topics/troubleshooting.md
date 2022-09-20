# Troubleshooting

In this section you will find ways to troubleshoot when you have problems executing CWL.
We focus on `cwltool` here but some of these techniques may apply to other CWL Runners.

## Run `cwltool` with `cachedir`

You can use the `--cachedir` option when running a workflow to tell `cwltool` to
cache intermediate files (files that are not input nor output files, but created
while your workflow is running). By default, these files are created in a
temporary directory but writing them to a separate directory makes accessing
them easier.

In the following example `troubleshooting-wf1.cwl` we have two steps, `step_a` and `step_b`.
These two steps are executed in order (we enforce it, see note below). The first step,
`step_a`, executes the `touch` command. The second step, `step_b`, **has a typo**,
where instead of also executing the `touch` command it tries to execute `ouch`, which
fails.

```{literalinclude} /_includes/cwl/troubleshooting/troubleshooting-wf1.cwl
:language: cwl
:name: "`troubleshooting-wf1.cwl`"
:caption: "`troubleshooting-wf1.cwl`"
:emphasize-lines: 25
```

```{note}
The CWL Standard does not guarantee the execution order of Workflow Steps. They can
be executed in any arbitrary order, or in paralell. So the in the `troubleshooting-wf1.cwl`
CWL document we enforce the order by chaining the output of `step_a` into an input
of `step_b`.
```

Let's execute this workflow with `/tmp/cachedir/` as the `--cachedir` value (`cwltool` will
create the directory for you if it does not exist already):

```{runcmd} cwltool --cachedir /tmp/cachedir/ troubleshooting-wf1.cwl
:working-directory: src/_includes/cwl/troubleshooting
:emphasize-lines: 12-14, 19-21
```

The workflow is in the `permanentFail` status due to `step_b` failing to execute the
non-existent `ouch` command. The `step_a` was executed successfully and its output
has been cached in your `cachedir` location. You can inspect the intermediate files
created:

```{runcmd} tree /tmp/cachedir
:emphasize-lines: 4
```

Each workflow step has received a unique ID (the long value that looks like a hash).
The `${HASH}.status` files display the status of each step executed by the workflow.
And the `step_a` output file `step_a.txt` is visible in the output of the command above.

Now fix the typo so `step_b` executes `touch` (i.e. replace `ouch` by `touch` in the
`step_b`). After fixing the typo, when you execute `cwltool` with the same arguments
as the previous time, note that now `cwltool` output contains information about
pre-cached outputs for `step_a`, and about a new cache entry for the output of `step_b`.
Also note that the status of `step_b` is now of success.

```{runcmd} cwltool --cachedir /tmp/cachedir/ troubleshooting-wf1-stepb-fixed.cwl
:working-directory: src/_includes/cwl/troubleshooting
:emphasize-lines: 12, 16-18
```

In this example the workflow step `step_a` was not re-evaluated as it had been cached, and
there was no change in its execution or output. Furthermore, `cwltool` was able to recognize
when it had to re-evaluate `step_b` after we fixed its executable name. This technique is
useful for troubleshooting your CWL documents and also as a way to prevent `cwltool` to
re-evaluate steps unnecessarily.
