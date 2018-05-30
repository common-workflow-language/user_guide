---
title: "File Formats"
teaching: 10
exercises: 0
questions:
- "How can I allow type-checking of input and output files?"
objectives:
- "Learn how to unambiguously specify the format of `File` objects."
keypoints:
- "You can document the expected format of input and output `File`s."
- "Once your tool is mature, we recommend specifying formats by referencing
existing ontologies e.g. EDAM."
---
Tools and workflows can take `File` types as input and produce them as output.
We also recommend indicating the format for `File` types. This helps document
for others how to use your tool while allowing you to do some simple
type-checking when creating parameter files.

For file formats, we recommend referencing existing ontologies (like EDAM in
our example), reference a local ontology for your institution, or do not add
a file format initially for quick development before sharing your tool with
others. You can browse existing file format listings for IANA [here][IANA] and
for EDAM [here][EDAM].

In the next tutorial, we explain  the `$namespace` and `$schema` section of the
document in greater detail, so don't worry about these for now.  

Note that for added value `cwltool` can do some basic reasoning based on file
formats and warn you if there seem to be some obvious mismatches.

*metadata_example.cwl*

~~~
{% include cwl/16-file-formats/metadata_example.cwl %}
~~~
{: .source}

The equivalent of this CWL description in command line format is:

`wc -l /path/to/aligned_sequences.ext > output.txt`

#### Sample Parameter Files

Below is an example of a parameter file for the example above. We encourage
checking in working examples of parameter files for your tool. This allows
others to quickly work with your tool, starting from a "known good"
parameterization.

*sample.yml*

~~~
{% include cwl/16-file-formats/sample.yml %}
~~~
{: .source}

___Note:___ To follow the example below, you need to download the example input file, *file-formats.bam*. The file is available from [https://github.com/common-workflow-language/user_guide/raw/gh-pages/_includes/cwl/16-file-formats/file-formats.bam
](https://github.com/common-workflow-language/user_guide/raw/gh-pages/_includes/cwl/16-file-formats/file-formats.bam) and can be downloaded e.g. via `wget`:

~~~
wget https://github.com/common-workflow-language/user_guide/raw/gh-pages/_includes/cwl/16-file-formats/file-formats.bam
~~~
{: .source}


Now invoke `cwl-runner` with the tool wrapper and the input object on the
command line:

~~~
$ cwltool metadata_example.cwl sample.yml
/usr/local/bin/cwltool 1.0.20161114152756
Resolved 'metadata_example.cwl' to 'file:///media/large_volume/testing/cwl_tutorial2/metadata_example.cwl'
[job metadata_example.cwl] /tmp/tmpNWyAd6$ /bin/sh \
    -c \
    'wc' '-l' '/tmp/tmpBf6m9u/stge293ac74-3d42-45c9-b506-dd35ea3e6eea/file-formats.bam' > /tmp/tmpNWyAd6/output.txt
Final process status is success
{
  "report": {
    "format": "http://edamontology.org/format_1964",
    "checksum": "sha1$49dc5004959ba9f1d07b8c00da9c46dd802cbe79",
    "basename": "output.txt",
    "location": "file:///media/large_volume/testing/cwl_tutorial2/output.txt",
    "path": "/media/large_volume/testing/cwl_tutorial2/output.txt",
    "class": "File",
    "size": 80
  }
}
~~~
{: .output}

[IANA]: https://www.iana.org/assignments/media-types/media-types.xhtml
[EDAM]: https://www.ebi.ac.uk/ols/ontologies/edam/terms?iri=http%3A%2F%2Fedamontology.org%2Fformat_1915
{% include links.md %}
