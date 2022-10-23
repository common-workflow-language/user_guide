#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: wc
arguments: ["-c"]
inputs:
  input_file:
    type: File
    arguments:
      position: 1
outputs: []
