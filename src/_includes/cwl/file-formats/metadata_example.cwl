#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool

label: An example tool demonstrating metadata.

inputs:
  aligned_sequences:
    type: File
    label: Aligned sequences in BAM format
    format: edam:format_2572
    inputBinding:
      position: 1

baseCommand: [ wc, -l ]

stdout: output.txt

outputs:
  report:
    type: stdout
    format: edam:format_1964
    label: A text file that contains a line count

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.18.owl
