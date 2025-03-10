#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: echo
inputs:
  example_flag:
    type: boolean
    arguments:
      position: 1
      prefix: -f
  example_string:
    type: string
    arguments:
      position: 3
      prefix: --example-string
  example_int:
    type: int
    arguments:
      position: 2
      prefix: -i
      separate: false
  example_file:
    type: File?
    arguments:
      prefix: --file=
      separate: false
      position: 4

outputs: []
