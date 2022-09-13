# File formats

Tools and workflows can take `File` types as input and produce them as output.
We also recommend indicating the format for `File` types. This helps document
for others how to use your tool while allowing you to do some simple
type-checking when creating parameter files.

For file formats, we recommend referencing existing ontologies (like EDAM in
our example), reference a local ontology for your institution, or do not add
a file format initially for quick development before sharing your tool with
others. You can browse existing file format listings for IANA [here][IANA] and
for EDAM [here][EDAM].

In the next tutorial, we explain  the `$namespaces` and `$schemas` section of the
document in greater detail, so don't worry about these for now.

Note that for added value `cwltool` can do some basic reasoning based on file
formats and warn you if there seem to be some obvious mismatches.

```{literalinclude} /_includes/cwl/file-formats/metadata_example.cwl
:language: cwl
:caption: "`metadata_example.cwl`"
:name: metadata_example.cwl
```

The equivalent of this CWL description in command line format is:

```{code-block} console
$ wc -l /path/to/aligned_sequences.ext > output.txt
```

## Sample Parameter Files

Below is an example of a parameter file for the example above. We encourage
checking in working examples of parameter files for your tool. This allows
others to quickly work with your tool, starting from a "known good"
parameterization.

```{literalinclude} /_includes/cwl/file-formats/sample.yml
:language: yaml
:caption: "`sample.yml`"
:name: sample.yml
```

___Note:___ To follow the example below, you need to download the example input file, *file-formats.bam*. The file is available from [https://github.com/common-workflow-language/user_guide/raw/main/_includes/cwl/file-formats/file-formats.bam
](https://github.com/common-workflow-language/user_guide/raw/main/_includes/cwl/file-formats/file-formats.bam) and can be downloaded e.g. via `wget`:

```{code-block}
$ wget https://github.com/common-workflow-language/user_guide/raw/main/_includes/cwl/file-formats/file-formats.bam
```

Now invoke `cwltool` with the tool description and the input object on the
command line:

```{runcmd} cwltool metadata_example.cwl sample.yml
:working-directory: src/_includes/cwl/file-formats/
```

[IANA]: https://www.iana.org/assignments/media-types/media-types.xhtml
[EDAM]: https://www.ebi.ac.uk/ols/ontologies/edam/terms?iri=http%3A%2F%2Fedamontology.org%2Fformat_1915
