# Inputs

## Essential Input Parameters

The `inputs` of a tool is a list of input parameters that control how to
run the tool.  Each parameter has an `id` for the name of parameter, and
`type` describing what types of values are valid for that parameter.

Available primitive types are *string*, *int*, *long*, *float*, *double*,
and *null*; complex types are *array* and *record*; in addition there are
special types *File*, *Directory* and *Any*.

The following example demonstrates some input parameters with different
types and how they can appear on the command line.

First, create a file called `inp.cwl`, containing the following:

```{literalinclude} /_includes/cwl/inputs/inp.cwl
:language: cwl
:caption: "`inp.cwl`"
:name: inp.cwl
```

Create a file called `inp-job.yml`:

```{literalinclude} /_includes/cwl/inputs/inp-job.yml
:language: yaml
:caption: "`inp-job.yml`"
:name: inp-job.yml
```

````{note}
You can use `cwltool` to create a template input object. That saves you from having
to type all the input parameters in an input object file:

```{runcmd} cwltool --make-template inp.cwl
:working-directory: src/_includes/cwl/inputs
```

You can redirect the output to a file, i.e. `cwltool --make-template inp.cwl > inp-job.yml`,
and then modify the default values with your desired input values.
````

Notice that "example_file", as a `File` type, must be provided as an
object with the fields `class: File` and `path`.

Next, create a whale.txt using [touch] by typing `touch whale.txt` on the command line.

```{code-block} console
$ touch whale.txt
```

Now, invoke `cwltool` with the tool description and the input object on the command line,
using the command `cwltool inp.cwl inp-job.yml`. The following boxed text describes these
two commands and the expected output from the command line:

```{runcmd} cwltool inp.cwl inp-job.yml
:working-directory: src/_includes/cwl/inputs
````

```{tip}
<p class="rubric">Where did those `/tmp` paths come from?</p>

The CWL reference runner (cwltool) and other runners create temporary
directories with symbolic ("soft") links to your input files to ensure that
the tools aren't accidentally accessing files that were not explicitly
specified
```

The field `inputBinding` is optional and indicates if and how the
input parameter should appear on the tool's command line. If
`inputBinding` is missing, the parameter does not appear on the command
line.  Let's look at each example in detail.

```cwl
example_flag:
  type: boolean
  inputBinding:
    position: 1
    prefix: -f
```

Boolean types are treated as a flag. If the input parameter
"example_flag" is "true", then `prefix` will be added to the
command line. If false, no flag is added.

```cwl
example_string:
  type: string
  inputBinding:
    position: 3
    prefix: --example-string
```

String types appear on the command line as literal values. The `prefix`
is optional, if provided, it appears as a separate argument on the
command line before the parameter. In the example above, this is
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
decimal text representation. When the option `separate` is false (the
default value is true), the prefix and value are combined into a single
argument. In the example above, this is rendered as `-i42`.


```cwl
example_file:
  type: File?
  inputBinding:
    prefix: --file=
    separate: false
    position: 4
```

File types appear on the command line as the path to the file. When the
parameter type ends with a question mark `?` it indicates that the
parameter is optional. In the example above, this is rendered as
`--file=/tmp/random/path/whale.txt`. However, if the "example_file"
parameter were not provided in the input, nothing would appear on the
command line.

Input files are read-only. If you wish to update an input file, you must
[first copy it to the output directory](staging-input-files.md).

The value of `position` is used to determine where the parameter should
appear on the command line.  Positions are relative to one another, not
absolute.  As a result, positions do not have to be sequential, three
parameters with positions 1, 3, 5 will result in the same command
line as 1, 2, 3.  More than one parameter can have the same position
(ties are broken using the parameter name), and the position field itself
is optional.  The default position is 0.

The `baseCommand` field will always appear in the final command line before the parameters.

[touch]: http://www.linfo.org/touch.html

### Optional Input Parameters

Optional input parameters must include `label` and `secondaryFiles`.
`label` is a short, human-readable description for the parameter.

```cwl
inputs:
  example_file:
    type: File
    label: Use case for label parameter
    inputBinding:
      position: 1
```

`secondaryFiles` is an optional input parameter that provides a pattern of specifying files
or directories that must be included alongside the primary file. 
The following example demonstrates the `secondaryFiles` input parameter.

```cwl
inputs:
  example_file:
    type: File
    secondaryFiles: [example_file.txt]
```

Also, a file object listed in `secondaryFiles` may contain nested `secondaryFiles` as shown below:

```{code-block} cwl
inputs:
  example_file:
    type: File
    secondaryFiles: [
            {
                example_file.txt
                secondaryFiles: [example_file_2.txt]
            }
        ]
```

Note that secondary files are only valid when `type` has a value `File`, or is an array of `items: File`.
All listed secondary files must be present in the same directory as the primary file,
since an implementation may fail workflow execution if a listed secondary file is not present. 

## Array Inputs

It is easy to add arrays of input parameters represented to the command
line. There are two ways to specify an array parameter. First is to provide
`type` field with `type: array` and `items` defining the valid data types
that may appear in the array. Alternatively, brackets `[]` may be added after
the `type: name` to indicate that the input parameter is an array of that type.

```{literalinclude} /_includes/cwl/inputs/array-inputs.cwl
:language: cwl
:caption: "`array-inputs.cwl`"
:name: array-inputs.cwl
```

```{literalinclude} /_includes/cwl/inputs/array-inputs-job.yml
:language: yaml
:caption: "`array-inputs-job.yml`"
:name: array-inputs-job.yml
```

Now invoke `cwltool` by providing the tool description and the input object
on the command line:

```{runcmd} cwltool array-inputs.cwl array-inputs-job.yml
:working-directory: src/_includes/cwl/inputs/
```

```{code-block} console
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

## Inclusive and Exclusive Inputs

Sometimes an underlying tool has several arguments that must be provided
together, (they are dependent) or several arguments that cannot be provided
together (they are exclusive).  You can use records and type unions to group
parameters together to describe these two conditions.

```{literalinclude} /_includes/cwl/inputs/record.cwl
:language: cwl
:caption: "`record.cwl`"
:name: record.cwl
```

```{literalinclude} /_includes/cwl/inputs/record-job1.yml
:language: yaml
:caption: "`record-job1.yml`"
:name: record-job1.yml
```

```{runcmd} cwltool record.cwl record-job1.yml
:working-directory: src/_includes/cwl/inputs/
:emphasize-lines: 6-7
```

In the first example, you can't provide `itemA` without also providing `itemB`.

```{literalinclude} /_includes/cwl/inputs/record-job2.yml
:language: yaml
:caption: "`record-job2.yml`"
:name: record-job2.yml
```

```{runcmd} cwltool record.cwl record-job2.yml
:working-directory: src/_includes/cwl/inputs
:emphasize-lines: 4, 10-11, 23
````

```{code-block} console
$ cat output.txt
-A one -B two -C three
```

In the second example, `itemC` and `itemD` are exclusive, so only the first
matching item (`itemC`) is added to the command line and remaining item (`itemD`) is ignored.

```{literalinclude} /_includes/cwl/inputs/record-job3.yml
:language: yaml
:caption: "`record-job3.yml`"
:name: record-job3.yml
```

```{runcmd} cwltool record.cwl record-job3.yml
:working-directory: src/_includes/cwl/inputs
:emphasize-lines: 9-10, 22
````

```{code-block} console
$ cat output.txt
-A one -B two -D four
```

In the third example, only `itemD` is provided, so it appears on the
command line.

### Exclusive Input Parameters with Expressions

If you use exclusive input parameters combined with expressions, you need to be
aware that the `inputs` JavaScript object will contain one of the exclusive
input values. This means that you might need to use an **or** boolean operator
to check which values are present.

Let's use an example that contains an exclusive `file_format` input parameter
that accepts `null` (i.e. no value provided), or any value from an enum.

```{literalinclude} /_includes/cwl/inputs/exclusive-parameter-expressions.cwl
:language: cwl
:caption: "`exclusive-parameter-expressions.cwl`"
:name: exclusive-parameter-expressions.cwl
```

Note how the JavaScript expression uses the value of the exclusive input parameter
without taking into consideration a `null` value. If you provide a valid value,
such as “fasta” (one of the values of the enum), your command should be executed
successfully:

```{runcmd} cwltool exclusive-parameter-expressions.cwl --file_format fasta
:working-directory: src/_includes/cwl/inputs
````

However, if you do not provide any input value, then `file_format` will be
evaluated to a `null` value, which does not match the expected type for the
output field (a `string`), resulting in failure when running your workflow.

```{runcmd} cwltool exclusive-parameter-expressions.cwl
:working-directory: src/_includes/cwl/inputs
:emphasize-lines: 5-10
```

To correct it, you must remember to use an **or** operator in your JavaScript expression
when using exclusive parameters, or any parameter that allows `null`. For example,
the expression could be changed to `$(inputs.file_format || 'auto')`, to have
a default value if none was provided in the command line or job input file.

% TODO
%
% - Explain its fields, such as default, valueFrom, etc. - https://github.com/common-workflow-language/common-workflow-language/issues/359
% - Optional Inputs https://github.com/common-workflow-language/user_guide/issues/44
% - Several ways of defining inputs/arguments to tools and workflows - https://github.com/common-workflow-language/user_guide/issues/33
% - Using an input output in another input - https://github.com/common-workflow-language/user_guide/issues/90
% - How to use linkMerge - https://github.com/common-workflow-language/user_guide/issues/117 (or maybe move to Advanced?)
