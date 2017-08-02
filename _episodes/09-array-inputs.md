---
title: "Array Inputs"
teaching: 10
exercises: 0
questions:
- "How do I specify input parameters in arrays?"
objectives:
- "Learn how to provide parameter arrays as input to a tool."
- "Learn how to control the organization of array parameters on the command
line."
keypoints:
- "Array parameter definitions are nested under the `type` field with
`type: array`."
- "The appearance of array parameters on the command line differs depending on
with the `inputBinding` field is provided in the description."
- "Use the `itemSeperator` field to control concatenatation of array
parameters."
---
It is easy to add arrays of input parameters represented to the command
line.  To specify an array parameter, the array definition is nested
under the `type` field with `type: array` and `items` defining the valid
data types that may appear in the array.

*array-inputs.cwl*

~~~
{% include cwl/array-inputs.cwl %}
~~~
{: .source}

*array-inputs-job.yml*

~~~
{% include cwl/array-inputs-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` providing the tool wrapper and the input object
on the command line:

~~~
$ cwl-runner array-inputs.cwl array-inputs-job.yml
[job 140334923640912] /home/example$ echo -A one two three -B=four -B=five -B=six -C=seven,eight,nine
-A one two three -B=four -B=five -B=six -C=seven,eight,nine
Final process status is success
{}
~~~
{: .output}

The `inputBinding` can appear either on the outer array parameter definition
or the inner array element definition, and these produce different behavior when
constructing the command line, as shown above.
In addition, the `itemSeperator` field, if provided, specifies that array
values should be concatenated into a single argument separated by the item
separator string.

You can specify arrays of arrays, arrays of records, and other complex
types.
