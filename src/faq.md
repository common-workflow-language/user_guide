# FAQ

% The items here do not look like questions, because we merged the
% How-Tos with the FAQ. We can/need to change it later.

```{contents}
:local:
:backlinks: "top"
```

## Non "`File`" Types Using `evalFrom`

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

## Rename an Input File

This example demonstrates how to change the name of an input file
as part of a tool description.
This could be useful when you are taking files produced from another
step in a workflow, and don't want to work with the default names that these
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

## Rename an Output File

This example demonstrates how to change the name of an output file
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

## Referencing a Local Script

There are two ways to reference a local script:

The first method involves adding the folder containing your scripts to the `PATH` environment variable.
This allows you to run the shell script directly without using `sh` or `bash` commands.

Start with adding a _shebang_ at the top of your file:

```{code-block}
#!/bin/bash
```

After that, make the script executable with the command `chmod +x scriptname.sh`

Finally, modify your `PATH` to add the directory where your script is located.
(It is good practice to use `$HOME/bin` for storing your own scripts).

```bash
export PATH=$PATH:$HOME/bin
```

Now you can use `baseCommand: scriptname.sh` to run the script directly.

```cwl
#!/bin/bash
cwlVersion: v1.0
class: CommandLineTool
baseCommand: scriptname.sh
```

When you wish to share your work later, you can place your script in a software container in the Docker format.

The second method involves including an input of `type: File` in the script itself:

```cwl
class: CommandLineTool

inputs:
  my_script:
     type: File
     inputBinding:
        position: 0


  # other inputs go here

baseCommand: sh

outputs: []
```

```{note}
In CWL, everything must be directly stated.
```

## Setting `self`-based Input Bindings for Optional Inputs

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

## Model a "one-or-the-other" Parameter

Below is an example showing how
to specify different strings to be added to a command line,
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

## Connect a Solo Value to an Input that Expects an Array of that Type

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

For command line flags that require a specific input as the argument an enum type can be declared in CWL. **Specifying null here is known as long form style. It does the same thing as the question mark on the other inputs.**

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

To properly set fields in a record input type, you need to pass a dictionary to the input to properly set the parameters. This is done by using inline JavaScript and returning the dictionary with the key of the field you want to set. The source field is set to indicate the input from the workflow to be used as the value.

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
## Concatenating Strings in Inputs

The valueFrom field must be used instead of default.

```yaml
input:
  valueFrom: |
     My String: $(input.stringvalue)
```

## `cwltool` Errors due to Filenames with Space Characters Inside

`cwltool` does not allow some characters in filenames by default.

For example, the filename `a space is here.txt` includes 3 space characters.

```console
ERROR Workflow error, try again with --debug for more information:

Invalid filename: 'a space is here.txt' contains illegal characters
```

If you can not avoid these dangerous characters, then pass `--relax-path-checks` to `cwltool`.

## CWL Parameter Reference Error due to Hyphen in Input Identifier

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


To fix this error, change `-` (hyphen) to `_` (underscore)

```cwl
valueFrom: $(inputs.sample_input)
                        # ^ changed here

...

inputs:
  sample_input: File
      # ^ changed here
```

If it is not possible to change the input identifier, then you can use an alternative CWL Parameter Reference syntax:

```cwl
valueFrom: $(inputs["sample-input"])
```

## Use CWL and cwltool with Singularity

<!-- https://matrix.to/#/!RQMxrGNGkeDmWHOaEs:gitter.im/$f1B-ytoep4PX3_tTgxaADRQFHGgisGiUL1nUHVQPBnY?via=gitter.im&via=matrix.org&via=gottliebtfreitag.de -->
The CWL standards are built around (optional) Docker format containers.
The reference runner and several other CWL implementations support running
those Docker format containers using the Singularity engine. Directly
specifying a Singularity format container is not part of the CWL standards.

## Debug JavaScript Expressions

You can use the <code>--js-console</code> option of <code>cwltool</code>, or you can try
creating a JavaScript or TypeScript project for your code, and load it
using <code>expressionLib</code>, e.g.: <a href="https://github.com/common-workflow-language/common-workflow-language/blob/master/v1.0/v1.0/template-tool.cwl#L6-L8">
https://github.com/common-workflow-language/common-workflow-language/blob/master/v1.0/v1.0/template-tool.cwl#L6-L8</a></dd>

% - https://github.com/common-workflow-language/user_guide/issues/6
% - Maybe adapt some of these (or move to a workaround?) https://www.synapse.org/#!Synapse:syn2813589/wiki/401464
