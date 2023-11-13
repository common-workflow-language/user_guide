#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["sh", "example.sh"]

requirements:
  InitialWorkDirRequirement:
    listing:
      - entryname: example.sh
        entry: |-
          PREFIX='Message is:'
          MSG="\${PREFIX} $(inputs.message)"
          echo \${MSG}

inputs:
  message: string
outputs:
  example_out:
    type: stdout
stdout: output.txt
