# Environment Variables

Tools run in a restricted environment and do not inherit most environment
variables from the parent process.  You can set environment variables for
the tool using `EnvVarRequirement`.

```{literalinclude} /_includes/cwl/12-env/env.cwl
:language: cwl
:caption: "`env.cwl`"
:name: env.cwl
```

```{literalinclude} /_includes/cwl/12-env/echo-job.yml
:language: yaml
:caption: "`echo-job.yml`"
```

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

```{code-block} console
$ cwl-runner env.cwl echo-job.yml
[job env.cwl] /home/example$ env > /home/example/output.txt
[job env.cwl] completed success
{
    "example_out": {
        "location": "file:///home/example/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$1ca16a840b14807b2fd3323022c476b06a150e2f",
        "size": 94,
        "path": "/home/example/output.txt"
    }
}
Final process status is success
$ cat output.txt
HELLO=Hello world!
PATH=/bin:/usr/bin:/usr/local/bin
HOME=/home/example
TMPDIR=/tmp/tmp63Obpk
```
