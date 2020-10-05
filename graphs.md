Graphs
------
Nodes (also called "verts", "vertexes", "vertices") are connected by edges
Edges _may_ have numeric weights associated with them
* If not shown, assume all weights are 1 ("unweighted graph")
Edges can be directed (one way) or undirected (two way)
* If there are _only_ undirected edges, we call it an "undirected graph"
* Else we call it a "directed graph"
Cycle: we can traverse and get back to the starting node somehow
* If a graph has any cycles in it, we call it a "cyclic graph".
* Else it's an "acyclic graph".
Representation of graphs
------------------------
Which nodes are adjacent ("directly connected") to a particular node.
Adjacency matrix
* Big grid that has true/false values showing which nodes are adjacent
  * Or edge weights
Adjacency list (what we'll use)
A: {B, D}
B: {D, C}
C: {C, B}
D: {}
BFT
---
Init:
    Add the starting vert to the queue
While the queue is not empty:
    Pop current vert off queue
    If not visited:
        "Visit" the node
        Track it as visited
        Add all its neighbors (adjacent nodes) to the queue
