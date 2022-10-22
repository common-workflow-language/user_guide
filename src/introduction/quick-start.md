# Quick Start

This section will show you a brief overview of what CWL is, and where you
can learn more about it. No previous knowledge of CWL is required, but you
must be comfortable following instructions for the command-line.

## “Hello World”

```{include} /_includes/what-is-cwl.md
```

CWL documents are written in [YAML](../topics/index.md) (and/or JSON).
The example below shows a simple CWL “Hello World” workflow annotated
with comments. Note that comments start with `#`:

```{literalinclude} /_includes/cwl/hello_world.cwl
:language: cwl
:name: hello_world.cwl
:caption: "`hello_world.cwl`"
```

The example above is just a wrapper for the `echo` command-line tool.
Running the workflow above with the default input values will produce the same result as the
command-line `echo "Hello World"`.

```{note}
In CWL, there is a distinction between a command-line tool and a workflow. But
for the sake of simplicity, we are using the term “workflow” here. You will learn
more about this in the [basic concepts](basic-concepts.md) section.
```

## Installing a CWL Runner

`cwltool` is an implementation of the CWL specification. It is also the
CWL *Reference Runner* for the specification, and it is compliant with the
latest version of the specification: {{ cwl_version }}. You can install
`cwltool` using `pip`:

```{code-block} console
:name: installing-cwltool-with-pip
:caption: Installing `cwltool` with `pip`.

$ pip install cwltool
```

```{note}
If installing the cwltool using the pip command doesn't work for you, the [prerequisites](prerequisites.md) section contains other ways to install `cwltool` and a more detailed list
of software and libraries used for following the rest of this user guide.
```

## Running "Hello World"

The usage of the `cwltool` command-line executable is basically
`cwltool [OPTIONS] <CWL_DOCUMENT> [INPUTS_OBJECT]`. You can run the
`hello_world.cwl` workflow without specifying any option:

```{runcmd} cwltool hello_world.cwl
:name: running-hello_world.cwl-with-cwltool
:caption: Running `hello_world.cwl` with `cwltool`.
```

Or you can override the default value of the input parameter `message`, similar
to how you would change the argument of the `echo` base command:

```{runcmd} cwltool hello_world.cwl --message="Hola mundo"
:name: running-hello_world.cwl-with-cwltool-passing-an-input-parameter
:caption: Running `hello_world.cwl` with `cwltool` passing an input parameter.
```

Another way of passing values to your workflow input parameters is via an
*Inputs Object*. This is a file containing the input fields with their
corresponding values. The Inputs Objects file can be written in JSON or YAML. For example:

```{literalinclude} /_includes/cwl/hello_world-job.json
:language: json
:name: hello_world-job.json
:caption: "`hello_world-job.json`"
```

You can use this Inputs Object file now to execute the “Hello World” workflow:

```{runcmd} cwltool hello_world.cwl hello_world-job.json
:name: passing-an-inputs-object-file-to-cwltool
:caption: Passing an Inputs Object file to `cwltool`.
```

```{note}
We used a similar file name for the workflow and for the Inputs Object files.
The *-job.json* suffix is very common in Inputs Object files, but it is not
a requirement. You can choose any name for your workflows and Inputs Object
files.
```

## Learn More

Continue reading the next sections of this User Guide!
- [List of CWL Implementations](https://www.commonwl.org/implementations).
- The [`common-workflow-language` organization](https://github.com/common-workflow-language) at GitHub.
- [Common Workflow Language at Wikipedia](https://en.wikipedia.org/wiki/Common_Workflow_Language).
- [YAML.org](http://yaml.org/) and [YAML at Wikipedia](https://en.wikipedia.org/wiki/YAML).
- The {{'[CWL Specification VERSION](https://www.commonwl.org/VERSION)'.replace('VERSION', cwl_version_text) }}.
- [Workflow management system at Wikipedia](https://en.wikipedia.org/wiki/Workflow_management_system).

% N.B.: Wondering what's up with this syntax in the CWL Specification link above?
% It's necessary as MyST Parser does not allow substitutions in links, for more:
% - https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-and-urls
% - https://github.com/executablebooks/MyST-Parser/issues/279
