# Metadata and authorship

Implementation extensions not required for correct execution (for example,
fields related to GUI presentation) and metadata about the tool or workflow
itself (for example, authorship for use in citations) may be provided as
additional fields on any object. Such extensions fields (e.g. `format: edam:format_2572`)
can use a namespace prefix listed in the `$namespaces` section of the document
(e.g. edam: http://edamontology.org/) as described in the [Schema Salad specification][schema-salad].
Once you add the namespace prefix, you can access it anywhere in the document as shown below.
Otherwise, one must use full URLs: `format: http://edamontology.org/format_2572`.


For all developers, we recommend the following minimal metadata for your tool
and workflows. This example includes metadata allowing others to cite your tool.

```{literalinclude} /_includes/cwl/metadata-and-authorship/metadata_example2.cwl
:language: cwl
:caption: "`metadata_example2.cwl`"
:name: metadata_example2.cwl
```

The equivalent of this CWL description in command line format is:

```{code-block}
$ wc -l /path/to/aligned_sequences.ext > output.txt
```

## Extended Example

For those that are highly motivated, it is also possible to annotate your tool
with a much larger amount of metadata. This example includes EDAM ontology tags
as keywords (allowing the grouping of related tools), hints at hardware
requirements in order to use the tool, and a few more metadata fields.

```{literalinclude} /_includes/cwl/metadata-and-authorship/metadata_example3.cwl
:language: cwl
:caption: "`metadata_example3.cwl`"
:name: metadata_example3.cwl
```

[schema-salad]: https://www.commonwl.org/v1.0/SchemaSalad.html#Explicit_context
