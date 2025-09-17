# Command Line Tool

A command-line tool is a type of Process object that can be run by
itself or as a Workflow step. It is a wrapper for a command like
`ls`, `echo`, `tar`, etc. The command-line tool is defined in the
`baseCommand` attribute of the command-line tool CWL document.

A CWL command-line tool must also have `inputs` and `outputs`.
The following example contains a minimal example of a CWL
command-line tool for the `echo` Linux command, using inputs and
outputs.

HOW COMMAND LINES WORK
The command line is a text interface for your computer. It’s a program that takes in commands, which it passes on to the computer’s operating system to run. From the command line, you can navigate through files and folders on your computer, just as you would with Windows Explorer on Windows or Finder on Mac OS. The difference is that the command line is fully text-based. Abbreviated as CLI, a Command Line Interface connects a user to a computer program or operating system. Through the CLI, users interact with a system or application by typing in text (commands). The command is typed on a specific line following a visual prompt from the computer. Abbreviated as CLI, a Command Line Interface connects a user to a computer program or operating system. Through the CLI, users interact with a system or application by typing in text (commands). The command is typed on a specific line following a visual prompt from the computer.





% TODO: Fix the missing link the graph below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: command-line-tool-graph

```{graphviz}
:caption: CWL command-line tool.
:align: center

digraph G {
    compound=true;
    rankdir="LR";
    fontname="Verdana";
    fontsize="10";
    graph [splines=ortho];

    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];

    subgraph cluster_0 {
      command[style="filled" label=<<FONT FACE='sans-serif;'>echo</FONT>>];
      label="baseCommand";
      fill=gray;
    }

    inputs -> command [lhead=cluster_0];
    command -> outputs [ltail=cluster_0];
}
```

% TODO: Fix the missing link the code below. We cannot have
%       it here as this file is included in two other files.
%       Sphinx prohibits it for the case where this could lead
%       to duplicate anchors in a page (e.g. single-html).
%       :name: echo.cwl

```{literalinclude} /_includes/cwl/echo.cwl
:language: cwl
:caption: "`echo.cwl`"
```
```{note}
The example above uses a simplified form to define inputs and outputs.You will learn more about in the [Inputs](../topics/inputs.md)
and in the [Outputs](../topics/outputs.md) sections.
```
% TODO
%
% - Spaces in commands https://github.com/common-workflow-language/user_guide/issues/39
% - Arguments (tell the reader the different use cases for arguments and inputs, tell them there is a section about inputs)
DIFFERENCES BEWTWEEN ARGUMENTS AND INPUTS 
Command line arguments are given to an application before it is run. For example First we give the app JavaProgram the command line arguments 30, 91, only then do we hit Enter and run it as a Java program. On the other hand, input can be given to an application during its run, because it can only ask for input after it started running. For that reason, we can print some text to the user before asking for input, indicating what input we are expecting for, etc.
The second difference is that Input can be taken any number of times. For that reason, input can be interactive - the system can take input, then respond according to it, then take more input, etc. Command line arguments are taken once, therefore can not be used to manage any interactiveness. 
You will learn more about inputs in section 2.4
USE CASES FOR THE COMMAND LINE ARGUMENTS
Command line arguments are extra commands you can use when launching a  program so that the program's functionality will change.  Depending on the program, these arguments can be used to add more features that includes specifying a file that output should be logged to, specifying a default document to launch, or to enable features that may be a bit buggy for normal use.
A command line argument is simply anything we enter after the executable name.  for example, if we launched Notepad using the command C:\Windows\System32\notepad.exe /s, then /s would be the command line argument we used.
It is important to note that you must add a space betten the program you want to run and the command line argument. For example notepad.exe/s is not a valid argument because it does not contain aspace. Instead  you must add a space so it looks like notpad.exe /s.

Available primitive types are string, int, long, float, double, and null; complex types are array and record; in addition there are special types File, Directory and Any.

The following example demonstrates some input parameters with different types and appearing on the command line in different ways.

First, create a file called inp.cwl, containing the following:

inp.cwl
#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
inputs:
  example_flag:
    type: boolean
    inputBinding:
      position: 1
      prefix: -f
  example_string:
    type: string
    inputBinding:
      position: 3
      prefix: --example-string
  example_int:
    type: int
    inputBinding:
      position: 2
      prefix: -i
      separate: false
  example_file:
    type: File?
    inputBinding:
      prefix: --file=
      separate: false
      position: 4

outputs: []

Sometimes tools require additional command line options that don’t correspond exactly to input parameters.

In this example, we will wrap the Java compiler to compile a java source file to a class file. By default, “javac” will create the class files in the same directory as the source file. However, CWL input files (and the directories in which they appear) may be read-only, so we need to instruct “javac” to write the class file to the designated output directory instead.

arguments.cwl
#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
label: Example trivial wrapper for Java 9 compiler
hints:
  DockerRequirement:
    dockerPull: openjdk:9.0.1-11-slim
baseCommand: javac
arguments: ["-d", $(runtime.outdir)]
inputs:
  src:
    type: File
    inputBinding:
      position: 1
outputs:
  classfile:
    type: File
    outputBinding:
      glob: "*.class"

## Network Access
This indicates whether a process requires outgoing IPv4/IPv6 network
access.  Starting with CWL v1.1, programs are not granted network
access by default, so you must include the requirement for network
access in the specification of your tool.

```cwl
cwlVersion: v1.2
class: CommandLineTool

requirements:
  NetworkAccess:
     networkAccess: true
```

```{note}
CWL v1.0 command-line tools that are upgraded to v1.1
or v1.2 or v1.2 will have `networkAccess: true` set automatically.
```
