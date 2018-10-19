---
title: "Introduction"
teaching: 0
exercises: 0
questions:
- "What is Common Workflow Language?"
- "Why might I want to learn to use CWL?"
objectives:
- "Learn what CWL is."
- "Learn about the motivation behind the project."
keypoints:
- "CWL describes command line tools and workflows."
- "CWL is not software."
- "Descriptions in CWL aid portability between environments"
---

CWL is a way to describe command line tools and connect them together to create
workflows.  Because CWL is a specification and not a specific piece of
software, tools and workflows described using CWL are portable across a variety
of platforms that support the CWL standard.

CWL has roots in "make" and many similar tools that determine order of
execution based on dependencies between tasks.  However unlike "make", CWL
tasks are isolated and you must be explicit about your inputs and outputs.  The
benefit of explicitness and isolation are flexibility, portability, and
scalability: tools and workflows described with CWL can transparently leverage
technologies such as Docker and be used with CWL implementations from different
vendors. CWL is well suited for describing large-scale workflows in cluster,
cloud and high performance computing environments where tasks are scheduled in
parallel across many nodes.

{% include links.md %}
