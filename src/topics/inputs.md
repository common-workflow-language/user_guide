# Inputs

## Essential Input Parameters

The `inputs` of a tool is a list of input parameters that control how to
run the tool.  Each parameter has an `id` for the name of parameter, and
`type` describing what types of values are valid for that parameter.

Available primitive types are *string*, *int*, *long*, *float*, *double*,
and *null*; complex types are *array* and *record*; in addition there are
special types *File*, *Directory* and *Any*.

The following example demonstrates some input parameters with different
types and appearing on the command line in different ways.

First, create a file called inp.cwl, containing the following:


```{literalinclude} /_includes/cwl/03-input/inp.cwl
:language: cwl
:caption: "`inp.cwl`"
:name: inp.cwl
```

Create a file called inp-job.yml:

*inp-job.yml*

```{literalinclude} /_includes/cwl/03-input/inp-job.yml
:language: yaml
:caption: "`inp-job.yml`"
:name: inp-job.yml
```

Notice that "example_file", as a `File` type, must be provided as an
object with the fields `class: File` and `path`.

Next, create a whale.txt using [touch] by typing `touch whale.txt` on the command line and then invoke `cwl-runner` with the tool description and the input object on the command line, using the command `cwl-runner inp.cwl inp-job.yml`. The following boxed text describes these two commands and the expected output from the command line:

```{code-block} console
$ touch whale.txt
$ cwl-runner inp.cwl inp-job.yml
[job inp.cwl] /tmp/tmpzrSnfX$ echo \
    -f \
    -i42 \
    --example-string \
    hello \
    --file=/tmp/tmpRBSHIG/stg979b6d24-d50a-47e3-9e9e-90097eed2cbc/whale.txt
-f -i42 --example-string hello --file=/tmp/tmpRBSHIG/stg979b6d24-d50a-47e3-9e9e-90097eed2cbc/whale.txt
[job inp.cwl] completed success
{}
Final process status is success
````

```{tip}
<p class="rubric">Where did those `/tmp` paths come from?</p>

The CWL reference runner (cwltool) and other runners create temporary
directories with symbolic ("soft") links to your input files to ensure that
the tools aren't accidentally accessing files that were not explicitly
specified
```

The field `inputBinding` is optional and indicates whether and how the
input parameter should appear on the tool's command line.  If
`inputBinding` is missing, the parameter does not appear on the command
line.  Let's look at each example in detail.

```cwl
example_flag:
  type: boolean
  inputBinding:
    position: 1
    prefix: -f
```

Boolean types are treated as a flag.  If the input parameter
"example_flag" is "true", then `prefix` will be added to the
command line.  If false, no flag is added.

```cwl
example_string:
  type: string
  inputBinding:
    position: 3
    prefix: --example-string
```

String types appear on the command line as literal values.  The `prefix`
is optional, if provided, it appears as a separate argument on the
command line before the parameter .  In the example above, this is
rendered as `--example-string hello`.

```cwl
example_int:
  type: int
  inputBinding:
    position: 2
    prefix: -i
    separate: false
```

Integer (and floating point) types appear on the command line with
decimal text representation.  When the option `separate` is false (the
default value is true), the prefix and value are combined into a single
argument.  In the example above, this is rendered as `-i42`.


```cwl
example_file:
  type: File?
  inputBinding:
    prefix: --file=
    separate: false
    position: 4
```

File types appear on the command line as the path to the file.  When the
parameter type ends with a question mark `?` it indicates that the
parameter is optional.  In the example above, this is rendered as
`--file=/tmp/random/path/whale.txt`.  However, if the "example_file"
parameter were not provided in the input, nothing would appear on the
command line.

Input files are read-only.  If you wish to update an input file, you must
[first copy it to the output directory](staging-input-files.md).

The value of `position` is used to determine where parameter should
appear on the command line.  Positions are relative to one another, not
absolute.  As a result, positions do not have to be sequential, three
parameters with positions 1, 3, 5 will result in the same command
line as 1, 2, 3.  More than one parameter can have the same position
(ties are broken using the parameter name), and the position field itself
is optional.  The default position is 0.

The `baseCommand` field will always appear in the final command line before the parameters.

[touch]: http://www.linfo.org/touch.html

## Array Inputs

It is easy to add arrays of input parameters represented to the command
line. There are two ways to specify an array parameter. First is to provide
`type` field with `type: array` and `items` defining the valid data types
that may appear in the array. Alternatively, brackets `[]` may be added after
the type name to indicate that input parameter is array of that type.

```{literalinclude} /_includes/cwl/09-array-inputs/array-inputs.cwl
:language: cwl
:caption: "`array-inputs.cwl`"
:name: array-inputs.cwl
```

```{literalinclude} /_includes/cwl/09-array-inputs/array-inputs-job.yml
:language: yaml
:caption: "`array-inputs-job.yml`"
:name: array-inputs-job.yml
```

Now invoke `cwl-runner` providing the tool description and the input object
on the command line:

```{code-block} console
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
```

The `inputBinding` can appear either on the outer array parameter definition
or the inner array element definition, and these produce different behavior when
constructing the command line, as shown above.
In addition, the `itemSeparator` field, if provided, specifies that array
values should be concatenated into a single argument separated by the item
separator string.

Note that the arrays of inputs are specified inside square brackets `[]` in `array-inputs-job.yml`. Arrays can also be expressed over multiple lines, where
array values that are not defined with an associated key are marked by a leading `-`.
This will be demonstrated in the next lesson
and is discussed in more detail in the [YAML Guide](yaml-guide.md#arrays).
You can specify arrays of arrays, arrays of records, and other complex types.

## Advanced Inputs

Sometimes an underlying tool has several arguments that must be provided
together (they are dependent) or several arguments that cannot be provided
together (they are exclusive).  You can use records and type unions to group
parameters together to describe these two conditions.

```{literalinclude} /_includes/cwl/11-records/record.cwl
:language: cwl
:caption: "`record.cwl`"
:name: record.cwl
```

```{literalinclude} /_includes/cwl/11-records/record-job1.yml
:language: yaml
:caption: "`record-job1.yml`"
:name: record-job1.yml
```

```{code-block} console
$ cwl-runner record.cwl record-job1.yml
Workflow error, try again with --debug for more information:
Invalid job input record:
record-job1.yml:1:1: the `dependent_parameters` field is not valid because
                       missing required field `itemB`
```

In the first example, you can't provide `itemA` without also providing `itemB`.

```{literalinclude} /_includes/cwl/11-records/record-job2.yml
:language: yaml
:caption: "`record-job2.yml`"
:name: record-job2.yml
```

```cwl
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
```

In the second example, `itemC` and `itemD` are exclusive, so only `itemC`
is added to the command line and `itemD` is ignored.

```{literalinclude} /_includes/cwl/11-records/record-job3.yml
:language: yaml
:caption: "`record-job3.yml`"
:name: record-job3.yml
```

```{code-block} console
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
```

In the third example, only `itemD` is provided, so it appears on the
command line.

% TODO
%
% - Explain its fields, such as default, valueFrom, etc. - https://github.com/common-workflow-language/common-workflow-language/issues/359
% - Exclusive parameters https://github.com/common-workflow-language/user_guide/issues/162
% - Optional Inputs https://github.com/common-workflow-language/user_guide/issues/44
% - Several ways of defining inputs/arguments to tools and workflows - https://github.com/common-workflow-language/user_guide/issues/33
% - Using an input output in another input - https://github.com/common-workflow-language/user_guide/issues/90
% - How to use linkMerge - https://github.com/common-workflow-language/user_guide/issues/117 (or maybe move to Advanced?)
% - Secondary files - https://github.com/common-workflow-language/common-workflow-language/issues/270
