from cwl_utils.parser.cwl_v1_2 import Process
from math import ceil

def create_processing_units_graph():
    processing_units = [pu.__qualname__ for pu in Process.__subclasses__()]
    processing_units.sort()
    # We want to have an elbow-edge between Process and its subclasses. So
    # first we decide whether we have an odd number of if we need one new
    # invisible node to balance the graph.
    hidden_nodes = ['n{}'.format(i) for i in range(0, len(processing_units))]
    extra_node_needed = len(processing_units) % 2 == 0
    if extra_node_needed:
        hidden_nodes.append('n{}'.format(len(processing_units)))
    node_in_the_middle = f'n{ceil(len(processing_units) / 2)}'
    nodes_links = hidden_nodes.copy()
    if extra_node_needed:
        nodes_links.remove(node_in_the_middle)

    # Template for the graphviz Sphinx directive.
    return f'''```{{graphviz}}
:name: processing-units-graph
:caption: The processing units available in the CWL objects model.
:align: center

digraph "A GraphViz graph with the CWL processing units, e.g. Process, Workflow, CommandLineTool, etc." {{
    rankdir="TB";
    graph [splines=false];

    node [fontname="Verdana", fontsize="10", shape=box];
    edge [fontname="Verdana", fontsize="10"];
    Process; {'; '.join([pu for pu in processing_units])};

    node[label="", width=0, height=0];
    edge[arrowhead=none];
    n1;

    {{rank=same; {'; '.join([node for node in processing_units])};}}
    Process -> n1 [arrowhead=normal, dir=back];
    {'; '.join([f'n1 -> {node}' for node in processing_units])};
}}
```'''


__all__ = [
    create_processing_units_graph
]
