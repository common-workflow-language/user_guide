cwlVersion: v1.2
class: CommandLineTool
requirements:
  - class: InlineJavascriptRequirement
    expressionLib:
      - { $include: custom-functions.js }
      - |
        /**
         * A merely illustrative example function that uses a function
         * from the included custom-functions.js file to create a
         * Hello World message.
         *
         * @param {Object} message - CWL document input message
         */
        var createHelloWorldMessage = function (message) {
          return capitalizeWords(message);
        };

baseCommand: echo

inputs:
  message:
    type: string

arguments: [$( createHelloWorldMessage(inputs.message) )]

outputs: []
