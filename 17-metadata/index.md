---
teaching: 10
exercises: 0
questions:
- "How do I make it easier for people to cite my tool descriptions?"
objectives:
- "Learn how to add authorship information and other metadata to a CWL
description."
keypoints:
- "Metadata can be provided in CWL descriptions."
- "Developers should provide a minimal amount of authorship information to
encourage correct citation."
---

# Metadata and Authorship

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

*metadata_example2.cwl*

```{literalinclude} /_includes/cwl/17-metadata/metadata_example2.cwl
:language: cwl
```

The equivalent of this CWL description in command line format is:

```bash
wc -l /path/to/aligned_sequences.ext > output.txt
```

## Extended Example

For those that are highly motivated, it is also possible to annotate your tool
with a much larger amount of metadata. This example includes EDAM ontology tags
as keywords (allowing the grouping of related tools), hints at hardware
requirements in order to use the tool, and a few more metadata fields.

*metadata_example3.cwl*

```{literalinclude} /_includes/cwl/17-metadata/metadata_example3.cwl
:language: cwl
```

[schema-salad]: https://www.commonwl.org/v1.0/SchemaSalad.html#Explicit_context
