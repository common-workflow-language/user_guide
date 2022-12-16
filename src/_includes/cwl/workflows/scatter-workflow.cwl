#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: Workflow

requirements:
  ScatterFeatureRequirement: {}

inputs:
  message_array: string[]

steps:
  echo:
    run: hello_world.cwl
    scatter: message
    in:
      message: message_array
    out: []

outputs: []
