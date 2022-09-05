# Troubleshooting

In this section you will find ways to troubleshoot when you have problems executing CWL,
specifically when using `cwltool` but some of these techniques may apply to different
CWL Runners as well.

## Run `cwltool` with `cachedir`

You can use the `--cachedir` option when running a workflow to tell `cwltool` to
cache intermediate files (files that are not input nor output files, but created
during runtime for the execution). By default, these files are created in the
temporary directory, but writing them to a separate directory makes it easier.

The following example `troubleshooting-wf1.cwl` has a **typo in the second step**,
where instead of calling `touch` is it calling `ouch`. We enforce the execution
of `step_a`, followed by `step_b`. This means that the `step_a.txt` is produced
before the `step_b` fails to produce a file.

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

Let's execute this workflow with `/tmp/cachedir/` as the `--cachedir` value (`cwltool` create the
directory for you if it does not already exist):

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

The workflow is in the `permanentFail` status, but you can inspect the intermediate
files created:

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

The `.status` files display the status of each step executed by the workflow. And
the `step_a.txt` is visible in the output. Note that `cwltool` shows what where
the workflow step outputs are being cached near “`Output of job will be cached (…)`”.

The next time you execute the same command, `cwltool` will use the cached output
of the workflow steps. Before doing so, fix the typo so `step_b` now runs `touch`.
After fixing the typo, when you execute `cwltool` with the same arguments as the
previous time, note that `cwltool` output will contain information about pre-cached
outputs, and about a new cache entry for the output of `step_b`.

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

In this example, the workflow step `step_a` was executed only once as its output was cached,
even though we executed `cwltool` twice. This can be useful for troubleshooting your CWL document,
while also avoiding recomputing steps.
