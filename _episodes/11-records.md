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

```
{% include cwl/record.cwl %}
```

*record-job1.yml*

```
{% include cwl/record-job1.yml %}
```

```
$ cwl-runner record.cwl record-job1.yml
Workflow error:
  Error validating input record, could not validate field `dependent_parameters` because
  missing required field `itemB`
```

In the first example, you can't provide `itemA` without also providing `itemB`.

*record-job2.yml*

```
{% include cwl/record-job2.yml %}
```

```
$ cwl-runner record.cwl record-job2.yml
[job 140566927111376] /home/example$ echo -A one -B two -C three
-A one -B two -C three
Final process status is success
{}
```

In the second example, `itemC` and `itemD` are exclusive, so only `itemC`
is added to the command line and `itemD` is ignored.

*record-job3.yml*

```
{% include cwl/record-job3.yml %}
```

```
$ cwl-runner record.cwl record-job3.yml
[job 140606932172880] /home/example$ echo -A one -B two -D four
-A one -B two -D four
Final process status is success
{}
```

In the third example, only `itemD` is provided, so it appears on the
command line.
