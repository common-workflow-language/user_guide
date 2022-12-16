#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
baseCommand: echo

requirements:
  InlineJavascriptRequirement: {}

inputs: []
outputs:
  example_out:
    type: stdout
stdout: output.txt
arguments:
  - prefix: -A
    valueFrom: $(1+1)
  - prefix: -B
    valueFrom: $("/foo/bar/baz".split('/').slice(-1)[0])
  - prefix: -C
    valueFrom: |
      ${
        var r = [];
        for (var i = 10; i >= 1; i--) {
          r.push(i);
        }
        return r;
      }
