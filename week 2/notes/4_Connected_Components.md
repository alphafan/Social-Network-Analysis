## Connected Components

__==>__ Check if a un-directed graph is connected in NetworkX
```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
                  ('B', 'K'), ('C', 'E'), ('C', 'F'), ('D', 'E'),
                  ('E', 'F'), ('E', 'H'), ('F', 'H'), ('I', 'J')])

print(nx.is_connected(G))
# False
print(nx.connected_components(G))
# [{'H', 'K', 'F', 'C', 'D', 'E', 'A', 'B'}, {'J', 'I'}]
print(nx.node_connected_component(G, 'A'))
# {'B', 'H', 'A', 'C', 'E', 'K', 'F', 'D'}
```

__==>__ Conditions of connected components
- Every node in a subset has the path to other nodes
- No other node has a path to any node in the subset

## Connectivity in `Directed Graph`
- Strongly connected graph
    - Every pair of nodes must ab able to go from u to v and v to u
    as well.
- Weakly connected graph
    - If we turns __directed graph__ --> __un-directed graph__ and it
    is connected, then it's weakly connected graph 

```python
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
                  ('B', 'K'), ('C', 'E'), ('C', 'F'), ('D', 'E'),
                  ('E', 'F'), ('E', 'H'), ('F', 'I'), ('I', 'J')])

print(nx.is_strongly_connected(G))
# False
print(nx.is_weakly_connected(G))
# True

print(list(nx.strongly_connected_components(G)))
print(list(nx.weakly_connected_components(G)))
```