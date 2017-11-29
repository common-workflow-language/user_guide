---
layout: page
title: "Recommended Practices"
permalink: /rec-practices/
---

Below are a set of recommended good practices to keep in mind when writing a Common Workflow Language description for a tool or workflow. These guidelines are presented for consideration on a scale of usefulness: more is better, not all are required.

&#9744; No `type: string` parameters for names of input or reference files/directories; use `type: File` or `type: Directory` as appropriate.

&#9744; Include a license that allows for re-use by anyone, e.g. [Apache 2.0][apache-license]. If possible, the license should be specified with its corresponding [SPDX identifier][spdx]. Construct the metadata field for the licence by providing a URL of the form `https://spdx.org/licenses/[SPDX-ID]` where `SPDX-ID` is the taken from the list of identifiers linked above. See the example snippet below for guidance. For non-standard licenses without an SPDX identifier, provide a URL to the license.

_Example of metadata field for license with SPDX identifier:_
~~~
$namespaces:
  s: http://schema.org/
s:license: https://spdx.org/licenses/Apache-2.0
# other s: declarations
~~~
{: .source}

For more examples of providing metadata within CWL descriptions, see the [Metadata and Authorship section][metadata-lesson] of this User Guide.

&#9744; Include [attribution information][license-example] for the author(s) of the CWL tool or workflow description. Use  unambiguous identifiers like [ORCID][orcid].

&#9744; In tool descriptions, list dependencies using short name(s) under `SoftwareRequirement`.

&#9744; Include [SciCrunch][scicrunch-issue] identifiers for dependencies in `https://identifiers.org/rrid/RRID:SCR_NNNNNN` format.

&#9744; All `input` and `output` identifiers should reflect their conceptual identity. Use informative names like `unaligned_sequences`, `reference_genome`, `phylogeny`, or `aligned_sequences` instead of  `foo_input`, `foo_file`, `result`, `input`, `output`, and so forth.

&#9744; In tool descriptions, include a list of version(s) of the tool that are known to work with this description under `SoftwareRequirement`.

&#9744; `format` should be specified for all input and output `File`s. Bioinformatics tools should use format identifiers from [EDAM][edam-example]. See also `iana:text/plain`, `iana:text/tab-separated-values` with `$namespaces: { iana: "https://www.iana.org/assignments/media-types/" }`. [Full IANA media type list][iana-types] (also known as MIME types). For non-bioinformatics tools use or build an appropriate ontology/controlled vocabulary in the same way. Please edit this page to let us know about it.

&#9744; Mark all input and output `File`s that are read from or written to in a streaming compatible way (only once, no random-access), as `streamable: true`.

&#9744; Each `CommandLineTool` description should focus on a single operation only, even if the (sub)command is capable of more. Don't overcomplicate your tool descriptions with options that you don't need/use.

&#9744; Custom types should be defined with one external YAML per type definition for re-use.

&#9744; Include a top level short `label` summarising the tool/workflow.

&#9744; If useful, include a top level `doc` as well. This should provide a longer, more detailed description than was provided in the top level `label` (see above).

&#9744; Use `type: enum` instead of `type: string` for elements with a fixed list of valid values.

&#9744; Evaluate all use of JavaScript for possible elimination or replacement. One common example: manipulating `File` names and paths? Consider whether one of the [built in `File` properties][file-prop] like `basename`, `nameroot`, `nameext`, etc, could be used instead.

&#9744; Give the tool description to a colleague (preferably at a different institution) to test and provide feedback.

&#9744; CWL implementations which also implement [`SubworkflowFeatureRequirement`][subworkflow] can support nesting workflows as a step within others. Complex workflows with individual components which can be abstracted should utilise this to make their workflow modular and allow sections of them to be easily reused.

[apache-license]: https://www.apache.org/licenses/LICENSE-2.0#apply
[license-example]: https://github.com/ProteinsWebTeam/ebi-metagenomics-cwl/blob/master/workflows/emg-assembly.cwl#L200
[scicrunch-issue]: https://github.com/common-workflow-language/common-workflow-language/issues/scicrunch.org
[edam-example]: http://edamontology.org/format_1915
[iana-types]: http://www.iana.org/assignments/media-types/media-types.xhtml
[file-prop]: http://www.commonwl.org/v1.0/CommandLineTool.html#File
[orcid]: https://orcid.org
[subworkflow]: http://www.commonwl.org/v1.0/Workflow.html#SubworkflowFeatureRequirement
[metadata-lesson]: /17-metadata/
