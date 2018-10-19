---
title: "Advanced Inputs"
teaching: 10
exercises: 0
questions:
- "How do I describe dependent and exclusive parameters?"
objectives:
- "Learn how to use records to describe the relationships between inputs."
keypoints:
- "Use the `record` field to group parameters together."
- "Multiple `record`s within the same parameter description are treated as
exclusive."
---
Sometimes an underlying tool has several arguments that must be provided
together (they are dependent) or several arguments that cannot be provided
together (they are exclusive).  You can use records and type unions to group
parameters together to describe these two conditions.

*record.cwl*

~~~
{% include cwl/11-records/record.cwl %}
~~~
{: .source}

*record-job1.yml*

~~~
{% include cwl/11-records/record-job1.yml %}
~~~
{: .source}

~~~
$ cwl-runner record.cwl record-job1.yml
Workflow error, try again with --debug for more information:
Invalid job input record:
record-job1.yml:1:1: the `dependent_parameters` field is not valid because
                       missing required field `itemB`
~~~
{: .output}

In the first example, you can't provide `itemA` without also providing `itemB`.

*record-job2.yml*

~~~
{% include cwl/11-records/record-job2.yml %}
~~~
{: .source}

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
{: .output}

In the second example, `itemC` and `itemD` are exclusive, so only `itemC`
is added to the command line and `itemD` is ignored.

*record-job3.yml*

~~~
{% include cwl/11-records/record-job3.yml %}
~~~
{: .source}

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
{: .output}

In the third example, only `itemD` is provided, so it appears on the
command line.

{% include links.md %}
