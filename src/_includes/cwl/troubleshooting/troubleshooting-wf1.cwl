cwlVersion: v1.2
class: Workflow

inputs: []
outputs: []

steps:
  step_a:
    run:
      class: CommandLineTool
      inputs: []
      outputs:
        step_a_file:
          type: File
          outputBinding:
            glob: 'step_a.txt'
      arguments: ['touch', 'step_a.txt']
    in: []
    out: [step_a_file]
  step_b:
    run:
      class: CommandLineTool
      inputs: []
      outputs: []
      arguments: ['ouch', 'step_b.txt']
    # To force step_b to wait for step_a
    in:
      step_a_file:
        source: step_a/step_a_file
    out: []
