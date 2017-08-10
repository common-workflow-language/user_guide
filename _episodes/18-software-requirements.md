---
title: "Specifying Software Requirements"
teaching: 10
exercises: 0
questions:
- "How do I specify requirements/dependencies for a job?"
- "What level of detail should I provide for a software requirement?"
objectives:
- "Learn how to write software requirement descriptions."
- "Learn how to use SciCrunch to retrieve a unique identifier for a tool/version
that is required."
keypoints:
- "Metadata can be provided in CWL descriptions."
- "Developers should provide a minimal amount of authorship information to
encourage correct citation."
---
Often tool descriptions will be written for a specific version of a software. To
make it easier for others to make use of your descriptions, you can include a
`SoftwareRequirement` field in the `hints` section.
This may also help to avoid confusion about which version of a tool the
description was written for.

~~~
{% include cwl/custom-types.cwl %}
~~~
{: .source}

In this example, the software requirement being described is InterProScan
version 5.21-60.

~~~
hints:
  SoftwareRequirement:
    packages:
      interproscan:
        specs: [ "https://identifiers.org/rrid/RRID:SCR_005829" ]
        version: [ "5.21-60" ]
~~~
{: .source}


[schema-salad]: http://www.commonwl.org/v1.0/SchemaSalad.html#Explicit_context
