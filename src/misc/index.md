# Miscellaneous

This is a collection of examples and short notes
about some operations that fall outside the scope of the User Guide
and/or have not yet been implemented in a clean way in the CWL standards.

## Non "`File`" types using `evalFrom`

```yaml
cwlVersion: v1.0  # or v1.1
class: CommandLineTool
requirements:
  InlineJavascriptRequirement: {}

baseCommand: [ echo, "42" ]

inputs: []

stdout: my_number.txt

outputs:
  my_number:
    type: int
    outputBinding:
       glob: my_number.txt
       loadContents: True
       outputEval: $(parselnt(self[0].contents))

  my_number_as_string:
    type: string
    outputBinding:
       glob: my_number.txt
       loadContents: True
       outputEval: $(self[0].contents)
```

## Rename an input file

This example shows how you can change the name of an input file
as part of a tool description.
This could be useful when you are taking files produced from another
step in a workflow and don't want to work with the default names that these
files were given when they were created.

```yaml
requirements:
  InitialWorkDirRequirement:
    listing:
      - entry: $(inputs.src1)
        entryName: newName
      - entry: $(inputs.src2)
        entryName: $(inputs.src1.basename)_custom_extension
```

## Rename an output file

This example shows how you can change the name an output file
from the default name given to it by a tool:

```yaml
cwlVersion: v1.0 # or v1.1
class: CommandLineTool
requirements:
  InlineJavascriptRequirement: {}

baseCommand: []

inputs: []

outputs:
 otu_table:
    type: File
    outputBinding:
      glob: otu_table.txt
      outputEval: ${self[0].basename=inputs.otu_table_name; return self;}
```

## Setting `self`-based input bindings for optional inputs

Currently, `cwltool` can't cope with missing optional inputs if their
input binding makes use of `self`.
Below is an example workaround for this,
pending a more sophisticated fix.

```yaml
#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

requirements: { InlineJavascriptRequirement: {} }

inputs:
  cfg:
    type: File?
    inputBinding:
      prefix: -cfg
      valueFrom: |
        ${ if(self === null) { return null;} else { return self.basename; } }

baseCommand: echo

outputs: []
```

## Model a "one-or-the-other" parameter

Below is an example of how
you can specify different strings to be added to a command line
based on the value given to a Boolean parameter.

```yaml
cwlVersion: v1.0
class: CommandLineTool
requirements:
  InlineJavascriptRequirement: {}
inputs:
  fancy_bool:
     type: boolean
     default: false  # or true
     inputBinding:
        valueFrom: ${if (self) { return "foo";} else { return "bar";}}

baseCommand: echo

outputs: []
```

## Connect a solo value to an input that expects an array of that type

Using [`MultipleInputFeatureRequirement`](https://www.commonwl.org/v1.0/Workflow.html#MultipleInputFeatureRequirement)
along with
[`linkMerge: merge_nested`](https://www.commonwl.org/v1.0/Workflow.html#WorkflowStepInput)

>   merge_nested
>
> The input must be an array consisting of exactly one entry for each input link.
> If "merge_nested" is specified with a single link, the value from the link must be wrapped in a single-item list.

Which means "create a list with exactly these sources as elements"

Or in other words: if the destination is of type `File[]` (an array of `File`s)
and the source is a single `File` then add `MultipleInputFeatureRequirement` to the Workflow level `requirements`
and add `linkMerge: merge_nested` under the appropriate `in` entry of the destination step.

```yaml
cwlVersion: v1.0
class: Workflow

requirements:
  MultipleInputFeatureRequirement: {}

inputs:
  readme: File

steps:
  first:
    run: tests/checker_wf/cat.cwl
    in:
     cat_in:  # type is File[]
       source: [ readme ]  # but the source is of type File
       linkMerge: merge_nested
    out: [txt]

outputs:
  result:
    type: File
    outputSource: first/txt
```
## Optional Inputs 💯

To make an input parameter optional, add a question mark to the type declaration.

```yaml
inputs:
  InputRead1:
    type: File
    inputBinding:
      position: 100

  #Optional Inputs
  isCasava:
    type: boolean?
    inputBinding:
      position: 1
      prefix: "--casava"
```
<a name="enuminputs"></a>
## Enum Inputs ⚜️

For commandline flags that require a specific input as the argument an enum type can be declared in CWL. **Specifying null here is known as long form style. It does the same thing as the question mark on the other inputs.**

```yaml
Format:
  type:
    - "null"
    - type: enum
      symbols:
        - bam
        - sam
        - bam_mapped
        - sam_mapped
        - fastq
  inputBinding:
    position: 2
    prefix: "--format"
```
<a name="recordinputs"></a>
## Record Inputs 📀

For commandline flags that are either **mutually exclusive** or **dependent** a special record type can be defined. You can also specify null here to create optional inputs.

```yaml
#Using record inputs to create mutually exclusive inputs

  Strand:
    type:
      - "null"
      - type: record
        name: forward
        fields:
          forward:
              type: boolean
              inputBinding:
                prefix: "--fr-stranded"

      - type: record
        name: reverse
        fields:
          reverse:
            type: boolean
            inputBinding:
              prefix: "--rf-stranded"

  PseudoBam:
    type: boolean?
    inputBinding:
      prefix: "--pseudobam"

#Using record inputs to create dependent inputs

  GenomeBam:
    type:
      - "null"
      - type: record
        name: genome_bam
        fields:
          genomebam:
            type: boolean
            inputBinding:
              prefix: "--genomebam"

          gtf:
            type: File
            inputBinding:
              prefix: "--gtf"

          chromosomes:
            type: File
            inputBinding:
              prefix: "--chromosomes"
```
## Setting Mutually Exclusive Parameters

In order to properly set fields in a record input type, you need to pass a dictionary to the input to properly set the parameters. This is done by using inline javascript and returning the dictionary with the key of the field you want to set. The source field is set to indicate the input from the workflow to be used as the value.

```yaml
steps:

  build_hisat2_index:
    run: ../Tools/Hisat2-Index.cwl
    in:
      InputFiles:
        source: FastaFiles
        valueFrom : |
          ${return {"fasta": self};}

      IndexName: IndexName

    out: [indexes]
```

## Setting Booleans

These can be set by using the default field
```yaml
input:
  default:true
```
## Concating Strings in Inputs

The valueFrom field must be used instead of default.

```yaml
input:
  valueFrom: |
     My String: $(input.stringvalue)
```

## `cwltool` errors due to filenames with space characters inside

`cwltool` does not allow some characters in filenames by default.

For example, the filename is `a space is here.txt` includes 3 space characters.

```console
ERROR Workflow error, try again with --debug for more information:

Invalid filename: 'a space is here.txt' contains illegal characters
```

If you can not avoid these dangerous characters, then pass `--relax-path-checks` to `cwltool`.

## CWL Parameter Reference error due to hyphen in input identifier

If `cwltool --validate` returns valid

```console
$ cwltool --validate cwl/qiime.cwl
INFO /usr/local/bin/cwltool 1.0.20190831161204
INFO Resolved 'cwl/qiime.cwl' to 'file:///workspace/cwl/qiime.cwl'
cwl/qiime.cwl is valid CWL.
```

But executing it causes an error like:

```console
$ cwltool cwl/qiime.cwl --sample-input metadata.tsv
INFO /usr/local/bin/cwltool 1.0.20190831161204
INFO Resolved 'cwl/qiime.cwl' to 'file:///workspace/cwl/qiime.cwl'
ERROR Workflow error, try again with --debug for more information:
cwl/qiime.cwl:14:5: Expression evaluation error:
                    Syntax error in parameter reference '(inputs.sample-input)'. This could be due
                    to using Javascript code without specifying InlineJavascriptRequirement.
```

The file is here

```cwl
cwlVersion: v1.0
class: CommandLineTool
baseCommand: [qiime, metadata, tabulate]
arguments:
  - prefix: --m-input-file
    valueFrom: $(inputs.sample-input)
inputs:
  sample-input: File
outputs: []
```

Problem caused by `-` (hyphen character).

```cwl
valueFrom: $(inputs.sample-input)
                        # ^ this is problem
...

inputs:
  sample-input: File
      # ^ this is problem
```


Fix this error is change `-` (hyphen) to `_` (underscore)

```cwl
valueFrom: $(inputs.sample_input)
                        # ^ changed here

...

inputs:
  sample_input: File
      # ^ changed here
```

If is not possible to change the input identifier, then you can use an alternative CWL Parameter Reference syntax:

```cwl
valueFrom: $(inputs["sample-input"])
```
