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
- "Use the `itemSeparator` field to control concatenatation of array
parameters."
---
It is easy to add arrays of input parameters represented to the command
line.  To specify an array parameter, the array definition is nested
under the `type` field with `type: array` and `items` defining the valid
data types that may appear in the array.

*array-inputs.cwl*

~~~
{% include cwl/09-array-inputs/array-inputs.cwl %}
~~~
{: .source}

*array-inputs-job.yml*

~~~
{% include cwl/09-array-inputs/array-inputs-job.yml %}
~~~
{: .source}

Now invoke `cwl-runner` providing the tool wrapper and the input object
on the command line:

~~~
$ cwl-runner array-inputs.cwl array-inputs-job.yml
[job array-inputs.cwl] /home/examples$ echo \
    -A \
    one \
    two \
    three \
    -B=four \
    -B=five \
    -B=six \
    -C=seven,eight,nine > /home/examples/output.txt
[job array-inputs.cwl] completed success
{
    "example_out": {
        "location": "file:///home/examples/output.txt",
        "basename": "output.txt",
        "class": "File",
        "checksum": "sha1$91038e29452bc77dcd21edef90a15075f3071540",
        "size": 60,
        "path": "/home/examples/output.txt"
    }
}
Final process status is success
$ cat output.txt
-A one two three -B=four -B=five -B=six -C=seven,eight,nine
~~~
{: .output}

The `inputBinding` can appear either on the outer array parameter definition
or the inner array element definition, and these produce different behavior when
constructing the command line, as shown above.
In addition, the `itemSeparator` field, if provided, specifies that array
values should be concatenated into a single argument separated by the item
separator string.

Note that the arrays of inputs are specified inside square brackets `[]` in `array-inputs-job.yml`. Arrays can also be expressed over multiple lines, where
array values that are not defined with an associated key is marked by a leading
`-`, as demonstrated in the next lesson. 
You can specify arrays of arrays, arrays of records, and other complex types.

{% include links.md %}
