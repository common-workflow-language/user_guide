# Best Practices

The following are a set of recommended good practices to keep in mind when writing a
Common Workflow Language description for a tool or workflow. These guidelines
are presented for consideration on a scale of usefulness: although more is better, not
all are required.

- No `type: string` parameters for names of input or reference
  files/directories; use `type: File` or `type: Directory` as appropriate.

- A CWL document (in conjunction with any external components like `Dockerfile`s) is software code.
  Workflow developers should be aware that the usual rules of software licensing apply to this
  document. For example, if the workflow is shared publicly, licensing terms must be clear so that
  a future user understands under what conditions they can run the workflow, modify it and/or
  combine it with other workflows. For this reason, please consider including a license field in the
  document. The authors of this guide urge you to choose a pre-existing license rather than trying
  to write your own (see the link below to learn more about choosing a license), and our recommended
  practice is to choose a license that allows for re-use by anyone, e.g. [Apache 2.0][apache-license].

  If possible, the license should be specified with its corresponding [SPDX identifier][spdx].
  Construct the metadata field for the license by providing a URL of the form
  `https://spdx.org/licenses/[SPDX-ID]` where `SPDX-ID` is taken from the list of identifiers
  linked above. See the example snippet below for guidance. For non-standard licenses without an SPDX
  identifier, provide a URL to the license.

  Useful reading: "[A Quick Guide to Software Licensing for the Scientist-Programmer][sci-license]"

  _Example of metadata field for license with SPDX identifier:_

  ```cwl
  $namespaces:
    s: https://schema.org/
  s:license: https://spdx.org/licenses/Apache-2.0
  # other s: declarations
  ```

  For more examples of providing metadata within CWL descriptions, see 
  [the Metadata and Authorship section of this User Guide](../topics/metadata-and-authorship.md).

- Include [attribution information][license-example] for the author(s) of
  the CWL tool or workflow description. Use unambiguous identifiers like
  [ORCID][orcid].

- In tool descriptions, list dependencies using short name(s) under
  `SoftwareRequirement`.

- Include [SciCrunch][scicrunch] identifiers for dependencies in
  `https://identifiers.org/rrid/RRID:SCR_NNNNNN` format.

- All `input` and `output` identifiers should reflect their conceptual
  identity. Use informative names like `unaligned_sequences`, `reference_genome`,
  `phylogeny`, or `aligned_sequences` instead of  `foo_input`, `foo_file`,
  `result`, `input`, `output`, and so forth.

- In tool descriptions, include a list of version(s) of the tool that are
  known to work with this description under `SoftwareRequirement`.

- `format` should be specified for all input and output `File`s.
  Bioinformatics tools should use format identifiers from [EDAM][edam-example].
  See also `iana:text/plain`, `iana:text/tab-separated-values` with
  `$namespaces: { iana: "https://www.iana.org/assignments/media-types/" }`.
  [Full IANA media type list][iana-types] (also known as MIME types). For
  non-bioinformatics tools, use or build an appropriate ontology/controlled
  vocabulary in the same way. Please edit this page to let us know about it.

- Mark all input and output `File`s that are read from or written to in a
  streaming compatible way (only once, no random-access), as `streamable: true`.

- Each `CommandLineTool` description should focus on a single operation
  only, even if the (sub)command is capable of more. Don't overcomplicate your
  tool descriptions with options that you don't need or use.

- Custom types should be defined with one external YAML per type
  definition for re-use.

- Include a top-level short `label` summarising the tool/workflow.

- If useful, include a top-level `doc` as well. This should provide a
  longer, more detailed description than was provided in the top-level `label`
  (see above).

- Use `type: enum` instead of `type: string` for elements with a fixed
  list of valid values.

- Evaluate all use of JavaScript for possible elimination or replacement.
  One common example: manipulating `File` names and paths? Consider whether one
  of the [built in `File` properties][file-prop] like `basename`, `nameroot`,
  `nameext`, etc., could be used instead.

- Give the tool description to a colleague (preferably at a different
  institution) to test and provide feedback.

- Complex workflows with individual components which can be abstracted
  should utilise the [`SubworkflowFeatureRequirement`][subworkflow] to make their
  workflow modular and allow sections of them to be easily reused.

- Software containers should be made to be conformant to the ["Recommendations for the packaging and containerizing of bioinformatics software"][containers] (also useful to other disciplines).

[containers]: https://doi.org/10.12688/f1000research.15140.1
[apache-license]: https://spdx.org/licenses/Apache-2.0.html
[license-example]: https://github.com/ProteinsWebTeam/ebi-metagenomics-cwl/blob/master/workflows/emg-assembly.cwl#L200
[scicrunch]: https://scicrunch.org
[edam-example]: http://edamontology.org/format_1915
[iana-types]: https://www.iana.org/assignments/media-types/media-types.xhtml
[file-prop]: https://www.commonwl.org/v1.0/CommandLineTool.html#File
[orcid]: https://orcid.org
[subworkflow]: https://www.commonwl.org/v1.0/Workflow.html#SubworkflowFeatureRequirement
[spdx]: https://spdx.org/licenses/
[sci-license]: https://doi.org/10.1371/journal.pcbi.1002598

% TODO
%
% - Writing CWL workflows (include existing docs from https://github.com/common-workflow-library/cwl-patterns/blob/main/README.md)
% - FAIR best practices with CWL
% - Docker best practices with CWL - https://github.com/common-workflow-language/common-workflow-language/issues/347
