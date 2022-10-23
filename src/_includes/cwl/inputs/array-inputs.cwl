#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
inputs:
  filesA:
    type: string[]
    arguments:
      prefix: -A
      position: 1

  filesB:
    type:
      type: array
      items: string
      arguments:
        prefix: -B=
        separate: false
    arguments:
      position: 2

  filesC:
    type: string[]
    arguments:
      prefix: -C=
      itemSeparator: ","
      separate: false
      position: 4

outputs:
  example_out:
    type: stdout
stdout: output.txt
baseCommand: echo
