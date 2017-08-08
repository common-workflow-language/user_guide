---
title: "Environment Variables"
teaching: 10
exercises: 0
questions:
- "How do I set the value of environment variables for a tool's execution?"
objectives:
- "Learn how to pass environment variables to a tool's runtime."
keypoints:
- "Tools run in a restricted environment with a minimal set of environment
variables."
- "Use the `EnvVarRequirement` field to set environment variables inside a
tool's environment."
---
Tools run in a restricted environment and do not inherit most environment
variables from the parent process.  You can set environment variables for
the tool using `EnvVarRequirement`.

*env.cwl*

~~~
{% include cwl/env.cwl %}
~~~
{: .source}

*echo-job.yml*

~~~
{% include cwl/echo-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ cwl-runner env.cwl echo-job.yml
[job 140710387785808] /home/example$ env
PATH=/bin:/usr/bin:/usr/local/bin
HELLO=Hello world!
TMPDIR=/tmp/tmp63Obpk
Final process status is success
{}
~~~
{: .output}
