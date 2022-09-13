#!/usr/bin/env cwltool

cwlVersion: v1.0
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
