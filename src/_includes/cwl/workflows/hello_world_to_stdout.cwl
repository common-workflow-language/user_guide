#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: echo
inputs:
  message:
    type: string
    arguments:
      position: 1
outputs: []
