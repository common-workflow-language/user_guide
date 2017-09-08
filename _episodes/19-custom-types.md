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

The example below is a CWL description of the [InterProScan][ips] tool for
simultaneously searching protein sequences against a wide variety of resources.
It is a good example of a number of good practices in CWL.

*custom-types.cwl*

~~~
{% include cwl/custom-types.cwl %}
~~~
{: .source}

*custom-types.yml*

~~~
{% include cwl/custom-types.yml %}
~~~
{: .source}

On line 34, in `inputs:applications`, a list of applications to be used in the
search are imported as a custom object:

```
inputs:
  proteinFile:
    type: File
    inputBinding:
      prefix: --input
  applications:
    type: InterProScan-apps.yml#apps[]?
    inputBinding:
      itemSeparator: ','
      prefix: --applications
```
{: .source}

The reference to a custom type is a combination of the name of the file in which
the object is defined (`InterProScan-apps.yml`) and the name of the object
within that file (`apps`) that defines the custom type. The square brackets `[]`
mean that an array of the preceding type is expected, in this case the `apps`
type from the imported `InterProScan-apps.yaml` file

The contents of the YAML file describing the custom type are given below:

~~~
{% include cwl/InterProScan-apps.yml %}
~~~
{: .source}

In order for the custom type to be used in the CWL description, it must be
imported. Imports are described in `requirements:SchemaDefRequirement`, as
below in the example `custom-types.cwl` description:

```
requirements:
  ResourceRequirement:
    ramMin: 10240
    coresMin: 3
  SchemaDefRequirement:
    types:
      - $import: InterProScan-apps.yml
```
{: .source}

Note also that the author of this CWL description has also included
`ResourceRequirement`s, specifying the minimum amount of RAM and number of cores
required for the tool to run successfully, as well as details of the version of
the software that the description was written for and other useful metadata.
These features are discussed further in other chapters of this user guide.

[ips]: https://github.com/ebi-pf-team/interproscan
