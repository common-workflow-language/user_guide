---
title: "Parameter References"
teaching: 10
exercises: 0
questions:
- "How do I reference input parameters in other fields?"
objectives:
- "Learn how to make parameter references in descriptions."
keypoints:
- "Some fields permit parameter references enclosed in `$(...)`."
- "References are written using a subset of Javascript syntax."
---
In a previous example, we extracted a file using the "tar" program.
However, that example was very limited because it assumed that the file
we were interested in was called "hello.txt".  In this example, you will
see how to reference the value of input parameters dynamically from other
fields.

*tar-param.cwl*

```
{% include cwl/tar-param.cwl %}
```

*tar-param-job.yml*

```
{% include cwl/tar-param-job.yml %}
```

Create your input files and invoke `cwl-runner` with the tool wrapper and the
input object on the command line:

```
$ rm hello.tar || true && touch goodbye.txt && tar -cvf hello.tar goodbye.txt
$ cwl-runner tar-param.cwl tar-param-job.yml
[job 139868145165200] $ tar xf /home/example/hello.tar goodbye.txt
Final process status is success
{
"example_out": {
  "location": "goodbye.txt",
  "size": 24,
  "class": "File",
  "checksum": "sha1$dd0a4c4c49ba43004d6611771972b6cf969c1c01"
  }
}
```

Certain fields permit parameter references which are enclosed in `$(...)`.
These are evaluated and replaced with value being referenced.

```
outputs:
  example_out:
    type: File
    outputBinding:
      glob: $(inputs.extractfile)
```

References are written using a subset of Javascript syntax.  In this
example, `$(inputs.extractfile)`, `$(inputs["extractfile"])`, and
`$(inputs['extractfile'])` are equivalent.

The value of the "inputs" variable is the input object provided when the
CWL tool was invoked.

Note that because `File` parameters are objects, to get the path to an
input file you must reference the path field on a file object; to
reference the path to the tar file in the above example you would write
`$(inputs.tarfile.path)`.
