cwlVersion: v1.2
class: Workflow


inputs:
  message: string
outputs: []

steps:
  echo:
    run: ../echo.cwl
    in:
      message: message
    out: [out]
  # Here you know you want an operation that changes the case of
  # the previous step, but you do not have an implementation yet.
  uppercase:
    run:
      class: Operation
      inputs:
        message: string
      outputs:
        uppercase_message: string
    in:
      message:
        source: echo/out
    out: [uppercase_message]
