# Prerequisites

% This page supersedes the old setup page: setup.md. We used that page as a reference while
% writing this documentation.

The software and configurations listed in this section are prerequisites for
following this user guide. The CWL standards are implemented by many different
workflow runners and platforms. This list of requirements focuses on the CWL reference runner,
`cwltool`. You can use another CWL-compatible runner or workflow system, but the results and
interface may look different (though the exact workflow outputs should be identical).

```{admonition} CWL Implementations

There are many implementations of the CWL standards. Some are complete CWL runners, while
others could be plug-ins or extensions to workflow engines. We have a better
explanation in the [Implementations](basic-concepts.md#implementations) section.
```

## Operating System

We recommend using an up-to-date operating system. You can choose any
of the following options for your operating system:

- Linux
- macOS
- Windows

```{note}
If you are using Windows, you will have to install the [Windows Subsystem for Linux 2](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL2).
Visit the `cwltool` [documentation](https://github.com/common-workflow-language/cwltool/blob/main/README.rst#ms-windows-users)
for details on installing WSL2.
Your operating system also needs internet access and a recent version of Python (3.6+).
```

## CWL Runner

% https://github.com/common-workflow-language/user_guide/issues/166
% https://github.com/common-workflow-language/user_guide/issues/64
% https://www.synapse.org/#!Synapse:syn2813589/wiki/401462

The first thing you will need for running CWL workflows is a CWL runner.
`cwltool` is a Python Open Source project maintained by the CWL community. It
is also the CWL reference runner, which means it must support everything in the
current CWL specification, {{ cwl_version }}.

`cwltool` can be installed with `pip`. We recommend using a virtual environment
like `venv` or `conda`. The following commands will create and activate a Python
virtual environment using the `venv` module, and install `cwltool` in that
environment:

```{code-block} console
:name: installing-cwltool-with-pip-and-venv
:caption: Installing `cwltool` with `pip` and `venv`.

$ python3 -m venv venv
$ source venv/bin/activate
$ (venv) pip install -U pip setuptools wheel
$ (venv) pip install cwltool
```

```{note}
You can find the `cwl-runner` [source code](https://github.com/common-workflow-language/cwltool/tree/main/cwlref-runner) in the `cwltool` repository.
Visit the `cwltool` [documentation](https://github.com/common-workflow-language/cwltool#install)
for other ways to install `cwltool` with `apt` and `conda`.
```
Let's use a simple CWL tool description `true.cwl` with `cwltool`.

```{literalinclude} /_includes/cwl/true.cwl
:language: yaml
:caption: "`true.cwl`"
:name: true.cwl
```

The `cwltool` command has an option to validate CWL tool and workflow descriptions. This option will parse the
CWL document, look for syntax errors, and verify that the workflow descriptions are compliant
with the CWL standards. However, these actions will be performed without running the document. To validate CWL workflows (or even a
standalone command line tool description like the above) pass the `--validate` option
to the `cwltool` command:

```{runcmd} cwltool --validate true.cwl
:name: validating-truecwl-with-cwltool
:caption: Validating `true.cwl` with `cwltool`.
```

You can run the CWL tool description by omitting the `--validate` option:

```{runcmd} cwltool true.cwl
:name: running-true.cwl-with-cwltool
:caption: Running `true.cwl` with `cwltool`.
```

### Cwl-runner Python Module

`cwl-runner` is an implementation-agnostic alias for CWL Runners. This simply means that the `cwl-runner` alias command can be invoked independently, and is not reliant on a particular CWL runner.
Users can invoke `cwl-runner` instead of invoking a CWL runner like `cwltool`
directly. The `cwl-runner` alias command then chooses the correct CWL runner.
This is convenient for environments with multiple CWL runners.

The CWL community publishes a Python package with the name `cwlref-runner` that installs
an alias for `cwltool` under the name `cwl-runner`

```{code-block} console
:name: installing-cwlrunner-with-pip
:caption: Installing `cwl-runner` alias for cwltool with `pip`.

$ pip install cwlref-runner
```

Now you can validate and run your workflow with the `cwl-runner` executable,
which will invoke `cwltool`. You should have the same results and output
as in the previous section.

```{runcmd} cwl-runner --validate true.cwl
:name: validating-true.cwl-with-cwl-runner
:caption: Validating `true.cwl` with `cwl-runner`.
```

```{runcmd} cwl-runner true.cwl
:name: running-true.cwl-with-cwl-runner
:caption: Running `true.cwl` with `cwl-runner`.
```

Another way to execute `cwl-runner` is by invoking the file directly. For that,
the first thing you need to do is copy `true.cwl` workflow into a new file:
`true_shebang.cwl`, and include a special first line, a *shebang*:

```{literalinclude} /_includes/cwl/true_shebang.cwl
:language: cwl
:name: "true_shebang.cwl"
:caption: "`true_shebang.cwl`"
```

Now you can make the file `true_shebang.cwl` executable with `chmod u+x`.

```{code-block} console
:name: making-true.cwl-executable
:caption: Making `true.cwl` executable.

$ chmod u+x true.cwl
```

And finally, you can execute it directly in the command-line. On execution, the program
specified in the shebang (`cwl-runner`) will be used to execute the
rest of the file.

```{runcmd} ./true_shebang.cwl
:name: running-true_shebang.cwl-with-a-shebang
:caption: Running `true_shebang.cwl` with a shebang.
```

```{note}
The *shebang* is the two-character sequence `#!` at the beginning of a
script. When the script is executable, the operating system will execute
the script using the executable specified after the shebang. It is
considered a good practice to use `/usr/bin/env <executable>` rather than using a hard-coded location, since `/usr/bin/env <executable>`
looks for the `<executable>` program in the system `PATH`, 
```

## Text Editor

You can use any text editor with CWL, but for syntax highlighting we recommend
an editor with YAML support. Popular editors are Visual Studio Code, Sublime,
WebStorm, vim/neovim, and Emacs.

There are extensions for Visual Studio Code and WebStorm that provide
integration with CWL, and features such as customized syntax highlighting and better
auto-complete:

- Visual Studio Code with the Benten (CWL) plugin - <https://github.com/rabix/benten#install-vs-code-extension>
- cwl-plugin for IntelliJ - <https://plugins.jetbrains.com/plugin/10040-cwl-plugin>

The CWL community also maintains a list of editors and viewers:
<https://www.commonwl.org/tools/#editors>

## Docker

% https://github.com/common-workflow-language/user_guide/issues/119

`cwltool` uses Docker to run tools, workflows, and workflow steps that specify a software container.
Follow the instructions in the Docker documentation to install it for your
operating system: <https://docs.docker.com/>.

You do not need to know how to write and build Docker containers. In the
rest of the user guide, we will use existing Docker images for running
examples, and to clarify the differences between the execution models
with and without containers.

```{note}
`cwltool` supports running containers with Docker, Podman, udocker, and
Singularity. You can also use alternative container registries for pulling
images.
```

## Learn More

- The [Implementations](basic-concepts.md#implementations) topic in the next section, Basic Concepts.
- The Python `venv` module: <https://docs.python.org/3/library/venv.html>
