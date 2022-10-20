# Using Containers

## Running Tools Inside Docker

[Docker][docker] containers simplify software installation by providing a
complete known-good runtime for software and its dependencies.  However,
containers are also purposefully isolated from the host system, so in
order to run a tool inside a Docker container there is additional work to
ensure that input files are available inside the container and output
files can be recovered from the container.  A CWL runner can perform this work
automatically, allowing you to use Docker to simplify your software
management while avoiding the complexity of invoking and managing Docker
containers.

One of the responsibilities of the CWL runner is to adjust the paths of
input files to reflect the location where they appear inside the container.

This example runs a simple Node.js script inside a Docker container which will
then print "Hello World" to the standard output.

```{literalinclude} /_includes/cwl/using-containers/docker.cwl
:language: cwl
:caption: "`docker.cwl`"
:name: docker.cwl
```

```{literalinclude} /_includes/cwl/using-containers/docker-job.yml
:language: yaml
:caption: "`docker-job.yml`"
:name: docker-job.yml
```

Before we run this, let's just break it down and see what some bits do.  Most of this
has been explained in previous sections, the only part that is really new is the `dockerRequirement`
section.

```cwl
baseCommand: node
hints:
  DockerRequirement:
    dockerPull: node:slim
```

`baseCommand: node` tells CWL that we will be running this command using the Node Js runtime that is meant for Javascript files. We
then need to specify some `hints` for how to find the container we want.  In this case we list
just our requirements for the docker container in `DockerRequirements`.  The `dockerPull:`
parameter takes the same value that you would pass to a `docker pull` command. That is,
the name of the container image (you can even specify the tag, which is good idea for
best practices when using containers for reproducible research). In this case we have
used a container called `node:slim`.

Create a Javascript file named "hello.js" and invoke `cwltool` providing the tool description and the
input object on the command line:

```{literalinclude} /_includes/cwl/using-containers/hello.js
:language: javascript
:caption: "`hello.js`"
:name: hello.js
```

```{runcmd} cwltool docker.cwl docker-job.yml
:working-directory: src/_includes/cwl/using-containers/
```

```{runcmd} cat output.txt
:working-directory: src/_includes/cwl/using-containers/
```

Notice the CWL runner has constructed a Docker command line to run the
script.

In this example, the path to the script `hello.js` is `/home/me/cwl/user_guide/hello.js`
outside the container but `/var/lib/cwl/job369354770_examples/hello.js` inside
the container, as reflected in the invocation of the `node` command.

[docker]: https://docker.io
