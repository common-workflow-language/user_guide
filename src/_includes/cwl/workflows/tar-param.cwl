#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: [tar, --extract]
inputs:
  tarfile:
    type: File
    arguments:
      prefix: --file
  extractfile:
    type: string
    arguments:
      position: 1
outputs:
  extracted_file:
    type: File
    outputBinding:
      glob: $(inputs.extractfile)
