---
title: "JavaScript Expressions"
teaching: 10
exercises: 0
questions:
- "What do I do when I want to create values dynamically and CWL doesn't
provide a built-in way of doing so?"
objectives:
- "Learn how to insert JavaScript expressions into a CWL description."
keypoints:
- "If `InlineJavascriptRequirement` is specified, you can include JavaScript
expressions that will be evaulated by the CWL runner."
- "Expressions are only valid in certain fields."
- "Expressions should only be used when no built in CWL solution exists."
---
If you need to manipulate input parameters, include the requirement
`InlineJavascriptRequirement` and then anywhere a parameter reference is
legal you can provide a fragment of Javascript that will be evaluated by
the CWL runner.

__Note: JavaScript expressions should only be used when absolutely necessary.
When manipulating file names, extensions, paths etc, consider whether one of the
[built in `File` properties][file-prop] like `basename`, `nameroot`, `nameext`,
etc, could be used instead.
See the [list of recommended practices][rec-practices].__

*expression.cwl*

~~~
{% include cwl/expression.cwl %}
~~~
{: .source}

As this tool does not require any `inputs` we can run it with an (almost) empty
job file:

*empty.yml*

~~~
{% include cwl/empty.yml %}
~~~
{: .source}

`empty.yml` contains a description of an empty JSON object. JSON objects
descriptions are contained inside curly brackets `{}`, so an empty object is
represented simply by a set of empyty brackets.

We can then run `expression.cwl`:

~~~
$ cwl-runner expression.cwl empty.yml
[job 140000594593168] /home/example$ echo -A 2 -B baz -C 10 9 8 7 6 5 4 3 2 1
-A 2 -B baz -C 10 9 8 7 6 5 4 3 2 1
Final process status is success
{}
~~~
{: .output}

You can only use expressions in certain fields.  These are:

- `filename`
- `fileContent`
- `envValue`
- `valueFrom`
- `glob`
- `outputEval`
- `stdin`
- `stdout`
- `coresMin`
- `coresMax`
- `ramMin`
- `ramMax`
- `tmpdirMin`
- `tmpdirMax`
- `outdirMin`
- `outdirMax`

[file-prop]: http://www.commonwl.org/v1.0/CommandLineTool.html#File
[rec-practices]: /rec-practices/
