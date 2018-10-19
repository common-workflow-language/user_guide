---
title: "Custom Types"
teaching: 10
exercises: 0
questions:
- "How do I create and import my own custom types into a CWL description?"
objectives:
- "Learn how to write custom CWL object types."
- "Learn how to import these custom objects into a tool description."
keypoints:
- "You can create your own custom types to load into descriptions."
- "These custom types allow the user to configure the behaviour of a tool
   without tinkering directly with the tool description."
- "Custom types are described in separate YAML files and imported as needed."
---

Sometimes you may want to write your own custom types for use and reuse in CWL
descriptions. Use of such custom types can reduce redundancy between multiple
descriptions that all use the same type, and also allow for additional
customisation/configuration of a tool/analysis without the need to fiddle with
the CWL description directly.

The example below is a CWL description of the [biom convert format][biom] tool for
converting a standard biom table file to hd5 format.

*custom-types.cwl*

~~~
{% include cwl/19-custom-types/custom-types.cwl %}
~~~
{: .source}

*custom-types.yml*

~~~
{% include cwl/19-custom-types/custom-types.yml %}
~~~
{: .source}

___Note:___ To follow the example below, you need to download the example input file, *rich_sparse_otu_table.biom*. The file is available from [https://raw.githubusercontent.com/common-workflow-language/user_guide/gh-pages/_includes/cwl/19-custom-types/rich_sparse_otu_table.biom](https://raw.githubusercontent.com/common-workflow-language/user_guide/gh-pages/_includes/cwl/19-custom-types/rich_sparse_otu_table.biom) and can be downloaded e.g. via `wget`:

~~~
wget https://raw.githubusercontent.com/common-workflow-language/user_guide/gh-pages/_includes/cwl/19-custom-types/rich_sparse_otu_table.biom
~~~
{: .source}

On line 34, in `inputs:table_type`, a list of allowable table options to be used in the
table conversion are imported as a custom object:

```
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
{: .source}

The reference to a custom type is a combination of the name of the file in which
the object is defined (`biom-convert-table.yaml`) and the name of the object
within that file (`table_type`) that defines the custom type. In this case the `symbols`
array from the imported `biom-convert-table.yaml` file define the allowable table options.
For example, in custom-types.yml, we pass `OTU table` as an `input` that 
tells the tool to create an OTU table in hd5 format. 

The contents of the YAML file describing the custom type are given below:

~~~
{% include cwl/19-custom-types/biom-convert-table.yaml %}
~~~
{: .source}

In order for the custom type to be used in the CWL description, it must be
imported. Imports are described in `requirements:SchemaDefRequirement`, as
below in the example `custom-types.cwl` description:

```
requirements:
  InlineJavascriptRequirement: {}
  ResourceRequirement:
    coresMax: 1
    ramMin: 100
  SchemaDefRequirement:
    types:
      - $import: biom-convert-table.yaml
```
{: .source}

Note also that the author of this CWL description has also included
`ResourceRequirement`s, specifying the minimum amount of RAM and number of cores
required for the tool to run successfully, as well as details of the version of
the software that the description was written for and other useful metadata.
These features are discussed further in other chapters of this user guide.

[biom]: http://biom-format.org/
{% include links.md %}
