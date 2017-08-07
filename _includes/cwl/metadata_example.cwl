#!/usr/bin/env cwl-runner

class: CommandLineTool
id: Example tool
label: Example tool
cwlVersion: v1.0
doc: |
    An example tool demonstrating metadata.

requirements:
  - class: ShellCommandRequirement

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
    edam: http://edamontology.org/
