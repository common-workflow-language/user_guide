#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: Workflow

requirements:
 ScatterFeatureRequirement: {}

inputs:
  message_array: string[]

steps:
  echo:
    run: hello_world_to_stdout.cwl
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
