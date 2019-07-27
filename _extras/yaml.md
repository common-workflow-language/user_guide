---
layout: page
title: "YAML Guide"
permalink: /yaml/
---

<script src="https://unpkg.com/mermaid@8.0.0/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>

[YAML][yaml-homepage] is a file format specification
designed to be readable by both computers and humans.
This guide introduces the features of YAML
relevant when writing CWL descriptions and inpout parameter files.

### Contents

- [Key-Value Pairs](/yaml/#key-value-pairs)
- [Comments](/yaml/#comments)
- [Mapped Objects](/yaml/#mapped-objects)
- [Arrays](/yaml/#arrays)
- [JSON Style](/yaml/#json-style)

### Key-Value Pairs

Fundamentally, a file written in YAML consists of a set of _key-value pairs_.
Each pair is written as `key: value`,
where whitespace before/after the `:` is optional.
Key names in CWL files should not contain whitespace -
We use [_camelCase_][camelCase] for multi-word key names
that have special meaning in the CWL specification
and underscored key names otherwise.
For example:

```yaml
first_name: Bilbo
last_name:  Baggins
age_years:  111
home:      Bag End, Hobbiton
```

The YAML above defines four keys -
`first_name`, `last_name`, `age_years`, and `home` -
with their four respective values.
Values can be
character strings,
numeric (integer, floating point, or scientfic representation),
Boolean (`true` or `false`),
or more complex nested types (see below).

### Comments

You may use `#` to add comments to your CWL and parameter files.
Any characters to the right of `#` will be ignored by the program interpreting
the YAML.
For example:

```yaml
first_name: Bilbo
last_name:  Baggins
age_years:  111
# this line will be ignored by the interpreter
home:      Bag End, Hobbiton # this is ignored too
```

### Mapped Objects

When describing a tool or workflow with CWL,
it is usually necessary to construct more complex, nested representations.
Called _maps_,
these hierarchical structures are described in YAML by providing
additional key-value pairs as the value of any key.
These pairs (sometimes referred to as "children") are written
on new lines under the key to which they belong (the "parent"),
and should be indented with two spaces
(tab characters are not allowed).
For example:

```yaml
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
inputs: # this key has an object value
  example_flag: # so does this one
    type: boolean
    inputBinding: # and this one too
      position: 1
      prefix: -f
```

The YAML above illustrates how you can build up complex nested object
descriptions relatively quickly.
The `inputs` map contains a single key, `example_flag`,
which itself contains two keys, `type` and `inputBinding`,
while one of these children, `inputBinding`,
contains a further two key-value pairs (`position` and `prefix`).
See the "Arrays" section below for more information about providing multiple
values/key-value pairs for a single key.
For comparison with the example YAML above,
here is a graphical representation of the `inputs` object it describes.

<div class="mermaid">
graph TD
  inputs --> example_flag
  example_flag --> type
  type --- bool((boolean))
  example_flag --> inputBinding
  inputBinding --> position
  inputBinding --> prefix
  position --- posval((1))
  prefix --- prefval(('-f'))
</div>

### Arrays

In certain circumstances it is necessary to provide
multiple values or objects for a single key.
As we've already seen in the "Mapped Objects" section above,
more than one key-value pair can be mapped to a single key.
However, it is also possible to define multiple values for a key
without having to provide a unique key for each value.
We can achieve this with an _array_,
where each value is defined on its own line and preceded by `-`.
For example:

```yaml
touchfiles:
  - foo.txt
  - bar.dat
  - baz.txt
```

and a more complex example combining maps and arrays:

```yaml
exclusive_parameters:
  type:
    - type: record
      name: itemC
      fields:
        itemC:
          type: string
          inputBinding:
            prefix: -C
    - type: record
      name: itemD
      fields:
        itemD:
          type: string
          inputBinding:
            prefix: -D
```

### JSON Style

YAML is based on [JavaScript Object Notation (JSON)][json]
and maps and arrays can also be defined in YAML using the native JSON syntax.
For example:

```yaml
touchfiles: [foo.txt, bar.dat, baz.txt] # equivalent to first Arrays example
```

and:

```yaml
# equivalent to the `inputs` example in "Mapped Objects" above
inputs: {example_flag: {type: boolean, inputBinding: {position: 1, prefix: -f}}}
```

Native JSON can be useful
to indicate where a field is being left intentionally empty
(such as `[]` for an empty array),
and where it makes more sense
for the values to be located on the same line
(such as when providing option flags and their values in a shell command).
However, as the second example above shows,
it can severely affect the readability of a YAML file
and should be used sparingly.

[camelCase]: https://en.wikipedia.org/wiki/Camel_case
[json]: http://json.org
[yaml-homepage]: http://yaml.org
