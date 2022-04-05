---
teaching: 10
exercises: 0
questions:
- "How do I describe which parameters must and must not be used in combination?"
objectives:
- "Learn how to use records to describe the relationships between inputs."
keypoints:
- "Use the `record` field to group parameters together."
- "Multiple `record`s within the same parameter description are treated as
exclusive."
---

# Advanced Inputs

Sometimes an underlying tool has several arguments that must be provided
together (they are dependent) or several arguments that cannot be provided
together (they are exclusive).  You can use records and type unions to group
parameters together to describe these two conditions.

*record.cwl*

```{literalinclude} /_includes/cwl/11-records/record.cwl
:language: yaml
```

*record-job1.yml*

```{literalinclude} /_includes/cwl/11-records/record-job1.yml
:language: yaml
```

~~~
$ cwl-runner record.cwl record-job1.yml
Workflow error, try again with --debug for more information:
Invalid job input record:
record-job1.yml:1:1: the `dependent_parameters` field is not valid because
                       missing required field `itemB`
~~~

In the first example, you can't provide `itemA` without also providing `itemB`.

*record-job2.yml*

```{literalinclude} /_includes/cwl/11-records/record-job2.yml
:language: yaml
```

~~~
$ cwl-runner record.cwl record-job2.yml
record-job2.yml:6:3: invalid field `itemD`, expected one of: 'itemC'
[job record.cwl] /home/example$ echo \
    -A \
    one \
    -B \
    two \
    -C \
    three > /home/example/output.txt
[job record.cwl] completed success
{
    "example_out": {
        "location": "file:///home/example/11-records/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$329fe3b598fed0dfd40f511522eaf386edb2d077",
        "size": 23,
        "path": "/home/example/output.txt"
    }
}
Final process status is success
$ cat output.txt
-A one -B two -C three
~~~

In the second example, `itemC` and `itemD` are exclusive, so only `itemC`
is added to the command line and `itemD` is ignored.

*record-job3.yml*

```{literalinclude} /_includes/cwl/11-records/record-job3.yml
:language: yaml
```

~~~
$ cwl-runner record.cwl record-job3.yml
[job record.cwl] /home/example$ echo \
    -A \
    one \
    -B \
    two \
    -D \
    four > /home/example/output.txt
[job record.cwl] completed success
{
    "example_out": {
        "location": "file:///home/example/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$77f572b28e441240a5e30eb14f1d300bcc13a3b4",
        "size": 22,
        "path": "/home/example/output.txt"
    }
}
Final process status is success
$ cat output.txt
-A one -B two -D four
~~~

In the third example, only `itemD` is provided, so it appears on the
command line.

```{include} ../_includes/links.md
```
