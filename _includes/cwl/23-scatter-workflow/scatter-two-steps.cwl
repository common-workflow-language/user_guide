#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow

requirements:
- class: ScatterFeatureRequirement

inputs:
  message_array: string[] 

steps:
  echo:
    run: 1st-tool-mod.cwl
    scatter: message
    in:
      message: message_array
    out: [echo_out]
  wc:
    run: wc-tool.cwl
    scatter: input_file
    in:
      input_file: echo/echo_out
    out: []

outputs: []
