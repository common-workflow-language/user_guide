#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: openjdk:9.0.1-11-slim
baseCommand: javac

requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.src)

inputs:
  src:
    type: File
    inputBinding:
      position: 1
      valueFrom: $(self.basename)

outputs:
  classfile:
    type: File
    outputBinding:
      glob: "*.class"
