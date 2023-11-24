# Environment Variables

Tools run in a restricted environment and do not inherit most environment
variables from the parent process.  You can set environment variables for
the tool using `EnvVarRequirement`.

```{literalinclude} /_includes/cwl/environment-variables/env.cwl
:language: cwl
:caption: "`env.cwl`"
:name: env.cwl
```

```{literalinclude} /_includes/cwl/environment-variables/echo-job.yml
:language: yaml
:caption: "`echo-job.yml`"
```

Now invoke `cwltool` with the tool description and the input object on the
command line:

```{runcmd} cwltool env.cwl echo-job.yml
:working-directory: src/_includes/cwl/environment-variables/
```

```{runcmd} cat output.txt
:working-directory: src/_includes/cwl/environment-variables/
```
