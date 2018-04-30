### What is a bipartie graph?

Bipartie graph is a graph where nodes can be split into two sets L and R 
and every edge connects an node in L with a node in R. No inner connections
inside L and R.

```python
from networkx.algorithms import bipartite
import networkx as nx

B = nx.Graph()
B.add_nodes_from(['A', 'B', 'C', 'D', 'E'], bipartite=0)
B.add_nodes_from(['1', '2', '3', '4', '5'], bipartite=1)
B.add_edges_from([('A', '1'), ('B', '1'), ('C', '1'), 
                  ('C', '3'), ('D', '2'), ('E', '3'),
                  ('E', '4'), ('E', '5')])
             
# Check if a graph is a bipartie graph
bipartite.is_bipartite(B)
# True
B.add_edge('A', 'B')
bipartite.is_bipartite(B)
# False
```

### How to detect if a graph is bipartie?

<img src='../images/32.png' />

Graph A is bipartite: the two sets of nodes are {A,B,C} and {E,G,F}. 
All edge connect a node in one set to a node in the other set. 

Graph B is not bipartite: note that nodes C, B, and F form a triangle, 
so it is not possible to assign each of these nodes to a side without 
having edges connecting nodes that were assigned to the same side. 

In fact, for the same reason, a bipartite graph cannot contain a 
cycle of an odd number of nodes.