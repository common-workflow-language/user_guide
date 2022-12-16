#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: Workflow

inputs: []

outputs:
  classout:
    type: File
    outputSource: compile/compiled_class

requirements:
  SubworkflowFeatureRequirement: {}

steps:
  compile:
    run: 1st-workflow.cwl
    in:
      tarball: create-tar/tar_compressed_java_file
      name_of_file_to_extract:
        default: "Hello.java"
    out: [compiled_class]

  create-tar:
    in: []
    out: [tar_compressed_java_file]
    run:
      class: CommandLineTool
      requirements:
        InitialWorkDirRequirement:
          listing:
            - entryname: Hello.java
              entry: |
                public class Hello {
                  public static void main(String[] argv) {
                      System.out.println("Hello from Java");
                  }
                }
      inputs: []
      baseCommand: [tar, --create, --file=hello.tar, Hello.java]
      outputs:
        tar_compressed_java_file:
          type: File
          streamable: true
          outputBinding:
            glob: "hello.tar"
