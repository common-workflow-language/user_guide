---
title: "Running Tools Inside Docker"
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
[Docker][docker] containers simplify software installation by providing a
complete known-good runtime for software and its dependencies.  However,
containers are also purposefully isolated from the host system, so in
order to run a tool inside a Docker container there is additional work to
ensure that input files are available inside the container and output
files can be recovered from the container.  CWL can perform this work
automatically, allowing you to use Docker to simplify your software
management while avoiding the complexity of invoking and managing Docker
containers.

This example runs a simple Node.js script inside a Docker container.

*docker.cwl*

```
{% include cwl/docker.cwl %}
```

*docker-job.yml*

```
{% include cwl/docker-job.yml %}
```

Provide a "hello.js" and invoke `cwl-runner` providing the tool wrapper and the
input object on the command line:

```
$ echo "console.log(\"Hello World\");" > hello.js
$ cwl-runner docker.cwl docker-job.yml
[job 140259721854416] /home/example$ docker run -i --volume=/home/example/hello.js:/var/lib/cwl/job369354770_examples/hello.js:ro --volume=/home/example:/var/spool/cwl:rw --volume=/tmp/tmpDLs5hm:/tmp:rw --workdir=/var/spool/cwl --read-only=true --net=none --user=1001 --rm --env=TMPDIR=/tmp node:slim node /var/lib/cwl/job369354770_examples/hello.js
Hello world!
Final process status is success
```

Notice the CWL runner has constructed a Docker command line to run the
script.  One of the responsibilities of the CWL runner is to adjust the paths of
input files to reflect the location where they appear inside the container.  
In this example, the path to the script `hello.js` is `/home/example/hello.js`
outside the container but `/var/lib/cwl/job369354770_examples/hello.js` inside
the container, as reflected in the invocation of the `node` command.

[docker]: https://docker.io