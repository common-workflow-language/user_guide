#!/usr/bin/env cwl-runner

class: CommandLineTool
id: Example tool
label: Example tool
cwlVersion: v1.0
doc: |
    An example tool demonstrating metadata. Note that this is an example and the metadata is not necessarily consistent.

requirements:
  - class: ShellCommandRequirement

hints:
  - class: ResourceRequirement
    coresMin: 4

inputs:
  bam_input:
    type: File
    doc: The BAM file used as input
    format: edam:format_2572
    inputBinding:
      position: 1

stdout: output.txt

outputs:
  report:
    type: File
    format: edam:format_1964
    outputBinding:
      glob: "*.txt"
    doc: A text file that contains a line count

baseCommand: ["wc", "-l"]

$namespaces:
- s: https://schema.org/
- edam: https://edamontology.org/

$schemas:
- https://schema.org/docs/schema_org_rdfa.html

s:author:
  - class: s:Person
    s:id: https://orcid.org/0000-0002-6130-1021
    s:email: mailto:dyuen@oicr.on.ca
    s:name: Denis Yuen

s:contributor:
  - class: s:Person
    s:id: http://orcid.org/0000-0002-7681-6415
    s:email: mailto:briandoconnor@gmail.com
    s:name: Brian O'Connor

s:citation: https://dx.doi.org/10.6084/m9.figshare.3115156.v2
s:codeRepository: https://github.com/common-workflow-language/common-workflow-language
s:dateCreated: "2016-12-13"
s:license: https://www.apache.org/licenses/LICENSE-2.0

s:keywords: edam:topic_0091 , edam:topic_0622
s:programmingLanguage: C
