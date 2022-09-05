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

```{code-block} cwl
:name: "`troubleshooting-wf1.cwl`"
:caption: "`troubleshooting-wf1.cwl`"
cwlVersion: v1.2
class: Workflow

inputs: []
outputs: []

steps:
  step_a:
    run:
      class: CommandLineTool
      inputs: []
      outputs:
        step_a_file:
          type: File
          outputBinding:
            glob: 'step_a.txt'
      arguments: ['touch', 'step_a.txt']
    in: []
    out: [step_a_file]
  step_b:
    run:
      class: CommandLineTool
      inputs: []
      outputs: []
      arguments: ['ouch', 'step_b.txt']
    # To force step_b to wait for step_a
    in:
      step_a_file:
        source: step_a/step_a_file
    out: []
```

```{note}
The CWL Standard does not guarantee the execution order of Workflow Steps. They can
be executed in any arbitrary order, or in paralell. So the in the `troubleshooting-wf1.cwl`
CWL document we enforce the order by chaining the output of `step_a` into an input
of `step_b`.
```

Let's execute this workflow with `/tmp/cachedir/` as the `--cachedir` value (`cwltool` will
create the directory for you if it does not exist already):

```{code-block} console
:emphasize-lines: 12-14, 19-21
$ cwltool --cachedir /tmp/cachedir/ troubleshoot_wf1.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220830195442
INFO Resolved 'troubleshoot_wf1.cwl' to 'file:///tmp/troubleshoot_wf1.cwl'
WARNING Workflow checker warning:
troubleshoot_wf1.cwl:28:7: 'step_a_file' is not an input parameter of ordereddict([('class',
                           'CommandLineTool'), ('inputs', []), ('outputs', []), ('arguments',
                           ['ouch', 'step_b.txt']), ('id',
                           '_:af6cdc76-ead7-4438-94a2-f9f96b3d70c5')]), expected
INFO [workflow ] start
INFO [workflow ] starting step step_a
INFO [step step_a] start
INFO [job step_a] Output of job will be cached in /tmp/cachedir/5504f8afaebc04b48f07e6e5f2b5237b
INFO [job step_a] /tmp/cachedir/5504f8afaebc04b48f07e6e5f2b5237b$ touch \
    step_a.txt
INFO [job step_a] completed success
INFO [step step_a] completed success
INFO [workflow ] starting step step_b
INFO [step step_b] start
INFO [job step_b] Output of job will be cached in /tmp/cachedir/feec39505ecca29dce1a210f75b12283
INFO [job step_b] /tmp/cachedir/feec39505ecca29dce1a210f75b12283$ ouch \
    step_b.txt
ERROR 'ouch' not found: [Errno 2] No such file or directory: 'ouch'
WARNING [job step_b] completed permanentFail
WARNING [step step_b] completed permanentFail
INFO [workflow ] completed permanentFail
{}
WARNING Final process status is permanentFail
```

The workflow is in the `permanentFail` status due to `step_b` failing to execute the
non-existent `ouch` command. The `step_a` was executed successfully and its output
has been cached in your `cachedir` location. You can inspect the intermediate files
created:

```{code-block} console
:emphasize-lines: 4
$ tree /tmp/cachedir
/tmp/cachedir
├── 5504f8afaebc04b48f07e6e5f2b5237b
│   └── step_a.txt
├── 5504f8afaebc04b48f07e6e5f2b5237b.status
├── abz3v9aq
├── feec39505ecca29dce1a210f75b12283
└── feec39505ecca29dce1a210f75b12283.status

3 directories, 3 files
```

Each workflow step has received a unique ID (the long value that looks like a hash).
The `${HASH}.status` files display the status of each step executed by the workflow.
And the `step_a` output file `step_a.txt` is visible in the output of the command above.

Now fix the typo so `step_b` executes `touch` (i.e. replace `ouch` by `touch` in the
`step_b`). After fixing the typo, when you execute `cwltool` with the same arguments
as the previous time, note that now `cwltool` output contains information about
pre-cached outputs for `step_a`, and about a new cache entry for the output of `step_b`.
Also note that the status of `step_b` is now of success.

```{code-block} console
:emphasize-lines: 12, 16-18
$ cwltool --cachedir /tmp/cachedir/ troubleshoot_wf1.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220830195442
INFO Resolved 'troubleshoot_wf1.cwl' to 'file:///tmp/troubleshoot_wf1.cwl'
WARNING Workflow checker warning:
troubleshoot_wf1.cwl:28:7: 'step_a_file' is not an input parameter of ordereddict([('class',
                           'CommandLineTool'), ('inputs', []), ('outputs', []), ('arguments',
                           ['touch', 'step_b.txt']), ('id',
                           '_:50e379f8-dce8-4794-9142-c53dc4e0e30d')]), expected
INFO [workflow ] start
INFO [workflow ] starting step step_a
INFO [step step_a] start
INFO [job step_a] Using cached output in /tmp/cachedir/5504f8afaebc04b48f07e6e5f2b5237b
INFO [step step_a] completed success
INFO [workflow ] starting step step_b
INFO [step step_b] start
INFO [job step_b] Output of job will be cached in /tmp/cachedir/822d8caf8894683f434ed8eb8be1b10d
INFO [job step_b] /tmp/cachedir/822d8caf8894683f434ed8eb8be1b10d$ touch \
    step_b.txt
INFO [job step_b] completed success
INFO [step step_b] completed success
INFO [workflow ] completed success
{}
INFO Final process status is success
```

In this example the workflow step `step_a` was not re-evaluated as it had been cached, and
there was no change in its execution or output. Furthermore, `cwltool` was able to recognize
when it had to re-evaluate `step_b` after we fixed its executable name. This technique is
useful for troubleshooting your CWL documents and also as a way to prevent `cwltool` to
re-evaluate steps unnecessarily.
