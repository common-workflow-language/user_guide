---
teaching: 10
exercises: 0
questions:
- "How do I run tools inside a Docker container?"
objectives:
- "Learn how to invoke tools inside a complete controlled runtime."
keypoints:
- "Containers can help to simplify management of the software requirements of
a tool."
- "Specify a Docker image for a tool with `DockerRequirement` in the `hints`
section."
---

# Running Tools Inside Docker

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

*docker.cwl*

```{literalinclude} /_includes/cwl/07-containers/docker.cwl
:language: cwl
```

*docker-job.yml*

```{literalinclude} /_includes/cwl/07-containers/docker-job.yml
:language: yaml
```

Before we run this, lets just break it down and see what some bits do.  Most of this
has been explained in previous sections, the only part that is really new is the `dockerRequirement`
section.

```cwl
baseCommand: node
hints:
  DockerRequirement:
    dockerPull: node:slim
```

`baseCommand: node` tells CWL that we will be running this command in a container. We
then need to specify some `hints` for how to find the container we want.  In this case we list
just our requirements for the docker container in `DockerRequirements`.  The `dockerPull:`
parameter takes the same value that you would pass to a `docker pull` command. That is,
the name of the container image (you can even specify the tag, which is good idea for
best practises when using containers for reproducible research). In this case we have
used a container called `node:slim`.


Provide a "hello.js" and invoke `cwl-runner` providing the tool wrapper and the
input object on the command line:

```bash
$ echo "console.log(\"Hello World\");" > hello.js
$ cwl-runner docker.cwl docker-job.yml
[job docker.cwl] /tmp/tmpgugLND$ docker \
    run \
    -i \
    --volume=/tmp/tmpgugLND:/var/spool/cwl:rw \
    --volume=/tmp/tmpSs5JoN:/tmp:rw \
    --volume=/home/me/cwl/user_guide/hello.js:/var/lib/cwl/job369354770_examples/hello.js:ro \
    --workdir=/var/spool/cwl \
    --read-only=true \
    --user=1000 \
    --rm \
    --env=TMPDIR=/tmp \
    --env=HOME=/var/spool/cwl \
    node:slim \
    node \
    /var/lib/cwl/job369354770_examples/hello.js > /tmp/tmpgugLND/output.txt
[job docker.cwl] completed success
{
    "example_out": {
        "location": "file:///home/me/cwl/user_guide/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$648a6a6ffffdaa0badb23b8baf90b6168dd16b3a",
        "size": 12,
        "path": "/home/me/cwl/user_guide/output.txt"
    }
}
Final process status is success
$ cat output.txt
Hello World
```

Notice the CWL runner has constructed a Docker command line to run the
script.

In this example, the path to the script `hello.js` is `/home/me/cwl/user_guide/hello.js`
outside the container but `/var/lib/cwl/job369354770_examples/hello.js` inside
the container, as reflected in the invocation of the `node` command.

[docker]: https://docker.io
