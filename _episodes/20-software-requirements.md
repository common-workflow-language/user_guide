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
- "Software requirements should be specified under `hints:SoftwareRequirement`."
---
Often tool descriptions will be written for a specific version of a software. To
make it easier for others to make use of your descriptions, you can include a
`SoftwareRequirement` field in the `hints` section.
This may also help to avoid confusion about which version of a tool the
description was written for.

~~~
{% include cwl/20-software-requirements/custom-types.cwl %}
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

Depending on your CWL runner, these hints may be used to check
that required software is installed and available before the job is run. To enable
these checks with the reference implementation, use the [dependency resolvers configuration][dependencies].

As well as a version number, a unique resource identifier (URI) for the tool is
given in the form of an [RRID][rrid]. Resources with RRIDs can be looked up in the
[SciCrunch][scicrunch] registry, which provides a portal for finding, tracking,
and referring to scientific resources consistently. If you want to specify a
tool as a `SoftwareRequirement`, search for the tool on SciCrunch and use the
RRID that it has been assigned in the registry. (Follow [this tutorial][scicrunch-add-tool]
if you want to add a tool to SciCrunch.) You can use this RRID to refer
to the tool (via [identifiers.org][identifiers]) in the `specs` field of your
requirement description. Other good choices, in order of preference, are to
include the DOI for the main tool citation and the URL to the tool.


[rrid]: https://scicrunch.org/resources/about/resource
[scicrunch]: https://scicrunch.org/
[dependencies]: https://github.com/common-workflow-language/cwltool#leveraging-softwarerequirements-beta
[identifiers]: https://identifiers.org/
[scicrunch-add-tool]: https://scicrunch.org/page/tutorials/336
{% include links.md %}
