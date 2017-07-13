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
[job tar-param.cwl] /tmp/tmpwH4ouT$ tar \
    xf \
    /tmp/tmpREYiEt/stgd7764383-99c9-4848-af51-7c2d6e5527d9/hello.tar \
    goodbye.txt
[job tar-param.cwl] completed success
{
    "example_out": {
        "checksum": "sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709", 
        "basename": "goodbye.txt", 
        "nameroot": "goodbye", 
        "nameext": ".txt", 
        "location": "file:///home/me/cwl/user_guide/goodbye.txt", 
        "path": "/home/me/cwl/user_guide/goodbye.txt", 
        "class": "File", 
        "size": 0
    }
}
Final process status is success
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
