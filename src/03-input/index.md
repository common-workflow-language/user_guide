---
teaching: 10
exercises: 0
questions:
- "How can I pass arguments to a command?"
- "How is the order of parameters defined for a command?"
objectives:
- "Learn how to describe and handle input parameters and files to a tool."
keypoints:
- "Inputs are described in the `inputs` section of a CWL description."
- "Files should be described with `class: File`."
- "You can use the `inputBinding` section to describe where and how an input
appears in the command."
orphan: true
---

```{attention}

This page is out-of-date and was kept here to preserve the links of the old
User Guide. The information on this page has been migrated to the
[Inputs](/core-concepts/inputs.md) section of the new user guide.
```

# Essential Input Parameters

The `inputs` of a tool is a list of input parameters that control how to
run the tool.  Each parameter has an `id` for the name of parameter, and
`type` describing what types of values are valid for that parameter.

Available primitive types are *string*, *int*, *long*, *float*, *double*,
and *null*; complex types are *array* and *record*; in addition there are
special types *File*, *Directory* and *Any*.

The following example demonstrates some input parameters with different
types and appearing on the command line in different ways.

First, create a file called inp.cwl, containing the following:


*inp.cwl*

```{literalinclude} /_includes/cwl/03-input/inp.cwl
:language: cwl
```

Create a file called inp-job.yml:

*inp-job.yml*

```{literalinclude} /_includes/cwl/03-input/inp-job.yml
:language: yaml
```

Notice that "example_file", as a `File` type, must be provided as an
object with the fields `class: File` and `path`.

Next, create a whale.txt using [touch] by typing `touch whale.txt` on the command line and then invoke `cwl-runner` with the tool wrapper and the input object on the command line, using the command `cwl-runner inp.cwl inp-job.yml`. The following boxed text describes these two commands and the expected output from the command line:

```bash
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
[first copy it to the output directory](/15-staging/index.md).

The value of `position` is used to determine where parameter should
appear on the command line.  Positions are relative to one another, not
absolute.  As a result, positions do not have to be sequential, three
parameters with positions 1, 3, 5 will result in the same command
line as 1, 2, 3.  More than one parameter can have the same position
(ties are broken using the parameter name), and the position field itself
is optional.  The default position is 0.

The `baseCommand` field will always appear in the final command line before the parameters.

[touch]: http://www.linfo.org/touch.html
