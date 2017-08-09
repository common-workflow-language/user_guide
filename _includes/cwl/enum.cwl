#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool

baseCommand: grep

inputs:
  directory_handling:
    inputBinding:
      position: 0
      prefix: --directories=
      separate: false
    type:
      type: enum
      symbols: [read, skip, recurse]
    default: read
  search_pattern:
    inputBinding:
      position: 1
    type: string
  search_target:
    inputBinding:
      position: 2
    type: Directory

outputs:
  output:
    type: stdout
