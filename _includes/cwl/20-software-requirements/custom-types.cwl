cwlVersion: v1.0
class: CommandLineTool

label: "InterProScan: protein sequence classifier"

doc: |
      Version 5.21-60 can be downloaded here:
      https://github.com/ebi-pf-team/interproscan/wiki/HowToDownload

      Documentation on how to run InterProScan 5 can be found here:
      https://github.com/ebi-pf-team/interproscan/wiki/HowToRun

requirements:
  ResourceRequirement:
    ramMin: 10240
    coresMin: 3
  SchemaDefRequirement:
    types:
      - $import: InterProScan-apps.yml

hints:
  SoftwareRequirement:
    packages:
      interproscan:
        specs: [ "https://identifiers.org/rrid/RRID:SCR_005829" ]
        version: [ "5.21-60" ]

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

baseCommand: interproscan.sh

arguments:
 - valueFrom: $(inputs.proteinFile.nameroot).i5_annotations
   prefix: --outfile
 - valueFrom: TSV
   prefix: --formats
 - --disable-precalc
 - --goterms
 - --pathways
 - valueFrom: $(runtime.tmpdir)
   prefix: --tempdir


outputs:
  i5Annotations:
    type: File
    format: iana:text/tab-separated-values
    outputBinding:
      glob: $(inputs.proteinFile.nameroot).i5_annotations

$namespaces:
 iana: https://www.iana.org/assignments/media-types/
 s: https://schema.org/
$schemas:
 - https://schema.org/docs/schema_org_rdfa.html

s:license: https://spdx.org/licenses/Apache-2.0
s:copyrightHolder: "EMBL - European Bioinformatics Institute"
