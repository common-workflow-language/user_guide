cwlVersion: v1.2
class: CommandLineTool

inputs:
  file_format:
    type:
      - 'null'
      - name: format_choices
        type: enum
        symbols:
          - auto
          - fasta
          - fastq
          - fasta.gz
          - fastq.gz
        inputBinding:
          position: 0
          prefix: '--format'
outputs:
  text_output:
    type: string
    outputBinding:
      outputEval: $(inputs.file_format)

baseCommand: 'true'
