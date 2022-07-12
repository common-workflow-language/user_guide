# Prerequisites

% This page supersedes the old setup.md. We used that page as reference while
% writing this documentation.

The software and configurations listed in this section are prerequisites for
following this user guide. The CWL Specification is implemented by multiple
CWL Runners. This list of requirements focuses on the `cwltool` runner. You
can use another CWL Runner but the examples may produce a different output.

```{admonition} CWL Implementations

There are many CWL Implementations. Some are complete CWL Runners,
others are plug-ins or extensions to Workflow Engines. We have a better
explanation in the [Basic Concepts](basic-concepts.md#implementations)
section.
```

## Operating System

We recommend using an up-to-date operating system. You can choose any
of the following options for your operating system:

- Linux
- macOS

You can try to use Window Subsystem for Linux 2 (WSL) to follow the
User Guide documentation, but some examples may not work as expected.

Your operating system also needs Internet access and a recent version
of Python 3.

## CWL runner

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

$ python -m venv venv
$ source venv/bin/activate
$ (venv) pip install cwltool
```

```{note}
Visit the `cwltool` [documentation](https://github.com/common-workflow-language/cwltool#install)
for other ways to install `cwltool` with `apt` and `conda`.
```

Let's use a simple workflow `true.cwl` with `cwltool`.

```{literalinclude} /_includes/cwl/simplest_cwl.cwl
:language: cwl
:caption: "`true.cwl`"
:name: true.cwl
```

The `cwltool` command has an option to validate CWL workflows. It will parse the
CWL workflow, look for syntax errors, and verify that the workflow is compliant
with the CWL specification, without running the workflow. To use it you just need
to pass `--validate` to the `cwltool` command:

% TODO: maybe figure out a way to avoid /home/kinow/ etc. in the documentation
%       to avoid multiple user-names/directory-locations varying in the docs.

```{code-block} console
:name: validating-truecwl-with-cwltool
:caption: Validating `true.cwl` with `cwltool`.

$ cwltool --validate true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220406080846
INFO Resolved 'true.cwl' to 'file:///tmp/true.cwl'
true.cwl is valid CWL.
```

You can run the CWL workflow now that you know it is valid:

```{code-block} console
:name: running-true.cwl-with-cwltool
:caption: Running `true.cwl` with `cwltool`.

$ cwltool true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwltool 3.1.20220406080846
INFO Resolved 'true.cwl' to 'file:///tmp/true.cwl'
INFO [job true.cwl] /tmp/f8xlh1pl$ true
INFO [job true.cwl] completed success
{}
INFO Final process status is success
```

### cwl-runner Python module

`cwl-runner` is an implementation agnostic alias for CWL Runners.
Users can invoke `cwl-runner` instead of invoking a CWL runner like `cwltool`
directly. The `cwl-runner` alias command then chooses the correct CWL runner.
This is convenient for environments with multiple CWL runners.

The CWL community publishes a Python module with the same name,
`cwl-runner`, that defaults to `cwltool`. `cwl-runner` will be used in
the rest of this user guide. You can use `pip` to install the `cwl-runner`
Python module:

```{code-block} console
:name: installing-cwlrunner-with-pip
:caption: Installing `cwl-runner` with `pip`.

$ pip install cwl-runner
```

% TODO: Maybe tell users where the cwl-runner source is? I couldn't find in PYPI as
%       it points to the CWL project: https://github.com/common-workflow-language/cwltool/tree/main/cwlref-runner

Now you can validate and run your workflow with `cwl-runner` executable,
which will invoke `cwltool`. You should have the same results and output
as in the previous section.

```{code-block} console
:name: validating-true.cwl-with-cwl-runner
:caption: Validating `true.cwl` with `cwl-runner`.

$ cwl-runner --validate true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwl-runner 3.1.20220406080846
INFO Resolved 'true.cwl' to 'file:///tmp/true.cwl'
true.cwl is valid CWL.
```

```{code-block} console
:name: running-true.cwl-with-cwl-runner
:caption: Running `true.cwl` with `cwl-runner`.

$ cwl-runner true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwl-runner 3.1.20220406080846
INFO Resolved 'true.cwl' to 'file:///tmp/true.cwl'
INFO [job true.cwl] /tmp/7a2gf1nh$ true
INFO [job true.cwl] completed success
{}
INFO Final process status is success
```

Another way to execute `cwl-runner` is invoking the file directly. For that,
the first thing you need is to modify the `true.cwl` workflow and include
a special first line, a *shebang*:

```{literalinclude} /_includes/cwl/simplest_cwl_shebang.cwl
:language: cwl
:name: cwltool-with-a-shebang
:caption: "`cwltool` with a shebang"
```

Now, after you make the file `true.cwl` executable with `chmod u+x`,
you can execute it directly in the command-line and the program
specified in the shebang (`cwl-runner`) will be used to execute the
rest of the file.

```{code-block} console
:name: making-true.cwl-executable-and-running-it
:caption: Making `true.cwl` executable and running it.

$ chmod u+x true.cwl
$ ./true.cwl
INFO /home/kinow/Development/python/workspace/user_guide/venv/bin/cwl-runner 3.1.20220406080846
INFO Resolved './true.cwl' to 'file:///tmp/true.cwl'
INFO [job true.cwl] /tmp/jz7ups99$ true
INFO [job true.cwl] completed success
{}
INFO Final process status is success
```

```{note}
The *shebang* is the two-character sequence `#!` at the beginning of a
script. When the script is executable, the operating system will execute
the script using the executable specified after the shebang. It is
considered a good practice to use `/usr/bin/env <executable>` since it
looks for the `<executable>` program in the system `PATH`, instead of
using a hard-coded location.
```

## Text Editor

You can use any text editor with CWL, but for syntax highlighting we recommend
an editor with YAML support. Popular editors are Visual Studio Code, Sublime,
WebStorm, vim/neovim, and Emacs.

There are extensions for Visual Studio Code and WebStorm that provide
integration with CWL, with customized syntax highlighting and better
auto-complete:

- Visual Studio Code with the Benten (CWL) plugin - <https://github.com/rabix/benten#install-vs-code-extension>
- cwl-plugin for IntelliJ - <https://plugins.jetbrains.com/plugin/10040-cwl-plugin>

The CWL community also maintains a list of editors and viewers:
<https://www.commonwl.org/#Editors_and_viewers>

## Docker

% https://github.com/common-workflow-language/user_guide/issues/119

`cwltool` uses Docker to run workflows or workflow steps with containers.
Follow the instructions in the Docker documentation to install it for your
operating system: <https://docs.docker.com/>.

You do not need to know how to write and build Docker containers. In the
rest of the user guide we will use existing Docker images for running
examples, and to clarify the differences between the execution models
with and without containers.

```{note}
`cwltool` supports running containers with Docker, Podman, udocker, and
Singularity. You can also use alternative container registries for pulling
images.
```

## Learn more

- The [Implementations](basic-concepts.md#implementations) topic
in the next section, Basic Concepts.
- The Python `venv` module: <https://docs.python.org/3/library/venv.html>
