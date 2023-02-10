#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: Workflow

requirements:
 ScatterFeatureRequirement: {}
 SubworkflowFeatureRequirement: {}

inputs:
  message_array: string[]

steps:
  subworkflow:
    run:
      class: Workflow
      inputs:
        message: string
      outputs: []
      steps:
        echo:
          run: hello_world_to_stdout.cwl
          in:
            message: message
          out: [echo_out]
        wc:
          run: wc-tool.cwl
          in:
            input_file: echo/echo_out
          out: []
    scatter: message
    in:
      message: message_array
    out: []
outputs: []
