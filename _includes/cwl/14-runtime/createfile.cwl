#!/usr/bin/env cwl-runner

class: CommandLineTool
cwlVersion: v1.0
baseCommand: ["cat", "example.conf"]

requirements:
  InitialWorkDirRequirement:
    listing:
      - entryname: example.conf
        entry: |
          CONFIGVAR=$(inputs.message)

inputs:
  message: string
outputs:
  example_out:
    type: stdout
stdout: output.txt
