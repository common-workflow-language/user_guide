cwlVersion: v1.2
class: Workflow

inputs:
  text:
    type: string
    default: 'Hello World'
outputs:
  reversed_message:
    type: string
    outputSource: step_b/reversed_message

steps:
  step_a:
    run:
      class: CommandLineTool
      stdout: stdout.txt
      inputs:
        text: string
      outputs:
        step_a_stdout:
          type: File
          outputBinding:
            glob: 'stdout.txt'
      arguments: ['echo', '-n', '$(inputs.text)']
    in:
      text: text
    out: [step_a_stdout]
  step_b:
    run:
      class: CommandLineTool
      stdout: stdout.txt
      inputs:
        step_a_stdout: File
      outputs:
        reversed_message:
          type: string
          outputBinding:
            glob: stdout.txt
            loadContents: true
            outputEval: $(self[0].contents)
      arguments: ['revv', '$(inputs.step_a_stdout)']
    in:
      step_a_stdout:
        source: step_a/step_a_stdout
    out: [reversed_message]
