# Recommended CWL Practices

Below are a set of recommended good practices to keep in mind when writing a Common Workflow Language description for a tool or workflow. These guidelines are presented for consideration on a scale of usefulness: more is better, not all are required.

- [ ] No `type: string` descriptions for names of input or reference files/directories.
- [ ] Include a license that allows for re-use by anyone, e.g. [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0#apply). [Example of license inclusion](https://github.com/ProteinsWebTeam/ebi-metagenomics-cwl/blob/master/workflows/emg-assembly.cwl#L200).
- [ ] Include [attribution information](https://github.com/ProteinsWebTeam/ebi-metagenomics-cwl/blob/master/workflows/emg-assembly.cwl#L200) for the CWL description author(s).
- [ ] In tool descriptions, list dependencies using short name(s) under `SoftwareRequirement`.
- [ ] Include [SciCrunch](https://github.com/common-workflow-language/common-workflow-language/issues/scicrunch.org) identifiers for dependencies in `https://identifiers.org/rrid/RRID:SCR_NNNNNN` format.
- [ ] All `input` and `output` identifiers should reflect their conceptual identity. No `foo_input`, `foo_file`, `result`, `input`, `output`, or other uninformative names.
- [ ] In tool descriptions, include a list of version(s) of the tool that are known to work.
- [ ] `format` should be specified for all input and output `File`s. Bioinformatics tools should use format identifiers from [EDAM](http://edamontology.org/format_1915). See also `iana:text/plain`, `iana:text/tab-separated-values` with `$namespaces: { iana: "https://www.iana.org/assignments/media-types/" }`. [Full IANA media type list](http://www.iana.org/assignments/media-types/media-types.xhtml) (also known as MIME types).
- [ ] Mark all input and output `File`s that are read or written to in a streaming compatible way (once, no random-access), as `streamable: true`.
- [ ] Each `CommandLineTool` description should focus on a single operation only, even if the (sub)command is capable of more.
- [ ] Custom types should be defined with one external YAML per type definition for re-use.
- [ ] Include a top level short `label` summarising the tool/workflow.
- [ ] If useful, include a top level `doc` as well. This should provide a longer, more detailed description than was provided in the top level `label` (see above).
- [ ] Use `type: enum` instead of `type: string` for elements with a fixed list of valid values.
- [ ] Evaluate all use of JavaScript for possible elimination or replacement. One common example: manipulating `File` names and paths? Consider whether one of the [built in `File` properties](http://www.commonwl.org/v1.0/CommandLineTool.html#File) like `basename`, `nameroot`, `nameext`, etc, could be used instead.
- [ ] Give the tool description to a colleague at a different institution to test and provide feedback.
