#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [tar, --extract]
inputs:
  tarfile:
    type: File
    arguments:
      prefix: --file
outputs:
  example_out:
    type: File
    outputBinding:
      glob: hello.txt
