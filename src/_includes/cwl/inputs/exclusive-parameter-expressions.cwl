cwlVersion: v1.2
class: CommandLineTool

inputs:
  output_format:
    type:
      - 'null'
      - name: output_format
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
      outputEval: $(inputs.output_format)

baseCommand: 'true'
