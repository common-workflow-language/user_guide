cwlVersion: v1.2
class: CommandLineTool
requirements:
  - class: InlineJavascriptRequirement
    expressionLib:
      - { $include: custom-functions.js }

baseCommand: echo

inputs:
  message:
    type: string

arguments: [$( capitalizeWords(inputs.message) )]

outputs: []
