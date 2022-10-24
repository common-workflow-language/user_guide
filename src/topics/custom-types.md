# Custom Types

Sometimes you may want to write your own custom types for use and reuse in CWL
descriptions. Use of such custom types can reduce redundancy between multiple
descriptions that all use the same type, and also allow for additional
customisation/configuration of a tool/analysis without the need to fiddle with
the CWL description directly.

The example below is a CWL description of the [biom convert format][biom] tool for
converting a standard biom table file to hdf5 format.

```{literalinclude} /_includes/cwl/custom-types/custom-types.cwl
:language: cwl
:caption: "`custom-types.cwl`"
:name: custom-types.cwl
```

```{literalinclude} /_includes/cwl/custom-types/custom-types.yml
:language: yaml
:caption: "`custom-types.yml`"
:name: custom-types.yml
```

___Note:___ To follow the example below, you need to [download the example input file](https://github.com/common-workflow-language/user_guide/blob/main/src/_includes/cwl/custom-types/rich_sparse_otu_table.biom), *rich_sparse_otu_table.biom* e.g. via `wget`:

```{code-block} console
$ wget https://github.com/common-workflow-language/user_guide/raw/main/src/_includes/cwl/custom-types/rich_sparse_otu_table.biom
```

On line 29, in `inputs:table_type`, a list of allowable table options to be used in the
table conversion are imported as a custom object:

```cwl
inputs:
  biom:
    type: File
    format: edam:format_3746  # BIOM
    inputBinding:
      prefix: --input-fp
  table_type:
    type: biom-convert-table.yaml#table_type
    inputBinding:
      prefix: --table-type
```

The reference to a custom type is a combination of the name of the file in which
the object is defined (`biom-convert-table.yaml`) and the name of the object
within that file (`table_type`) that defines the custom type. In this case the `symbols`
array from the imported `biom-convert-table.yaml` file define the allowable table options.
For example, in `custom-types.yml`, we pass `OTU table` as an `input` that
tells the tool to create an OTU table in hdf5 format.

The contents of the YAML file describing the custom type are given below:

```{literalinclude} /_includes/cwl/custom-types/biom-convert-table.yaml
:language: yaml
:caption: "`biom-convert-table.yaml`"
:name: biom-convert-table.yaml
```

In order for the custom type to be used in the CWL description, it must be
imported. Imports are described in `requirements:SchemaDefRequirement`, as
below in the example `custom-types.cwl` description:

```cwl
requirements:
  InlineJavascriptRequirement: {}
  ResourceRequirement:
    coresMax: 1
    ramMin: 100
  SchemaDefRequirement:
    types:
      - $import: biom-convert-table.yaml
```

Note also that the author of this CWL description has also included
`ResourceRequirement`s, specifying the minimum amount of RAM and number of cores
required for the tool to run successfully, as well as details of the version of
the software that the description was written for and other useful metadata.
These features are discussed further in other chapters of this user guide.

[biom]: http://biom-format.org/

% TODO (enums)
%
% - https://github.com/common-workflow-language/user_guide/issues/155
% - Maybe show an example with booleans, pros and cons - https://github.com/common-workflow-language/user_guide/issues/89
%
% TODO (records)
%
% - https://github.com/common-workflow-language/common-workflow-language/issues/202
% - Document corner cases & workarounds - https://github.com/common-workflow-language/common-workflow-language/issues/241
