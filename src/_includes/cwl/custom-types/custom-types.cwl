#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool

requirements:
  InlineJavascriptRequirement: {}
  ResourceRequirement:
    coresMax: 1
    ramMin: 100  # just a default, could be lowered
  SchemaDefRequirement:
    types:
      - $import: biom-convert-table.yaml

hints:
  DockerRequirement:
    dockerPull: 'quay.io/biocontainers/biom-format:2.1.6--py27_0'
  SoftwareRequirement:
    packages:
      biom-format:
        specs: [ "https://doi.org/10.1186/2047-217X-1-7" ]
        version: [ "2.1.6" ]

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

  header_key:
    type: string?
    doc: |
      The observation metadata to include from the input BIOM table file when
      creating a tsv table file. By default no observation metadata will be
      included.
    inputBinding:
      prefix: --header-key

baseCommand: [ biom, convert ]

arguments:
  - valueFrom: $(inputs.biom.nameroot).hdf5
    prefix: --output-fp
  - --to-hdf5

outputs:
  result:
    type: File
    outputBinding: { glob: "$(inputs.biom.nameroot)*" }

$namespaces:
  edam: http://edamontology.org/
  s: https://schema.org/

$schemas:
  - http://edamontology.org/EDAM_1.16.owl
  - https://schema.org/version/latest/schemaorg-current-http.rdf

s:license: https://spdx.org/licenses/Apache-2.0
s:copyrightHolder: "EMBL - European Bioinformatics Institute"
