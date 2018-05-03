## Path
A sequence of node connected by an edge

## Distance
__==> Q:__ How far is a node from another node?
- A: Shortest path length

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
                  ('B', 'K'), ('C', 'E'), ('C', 'F'), ('D', 'E'),
                  ('E', 'F'), ('E', 'H'), ('F', 'G'), ('I', 'J')])

print(nx.shortest_path(G, 'A', 'E'))
print(nx.shortest_path_length(G, 'A', 'E'))
```

__==> Q:__ How to find the distance from a node to `ALL` the other nodes?
- Not possible to do it in real large network.
- Breadth first search (similar to layers order visit)

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
                  ('B', 'K'), ('C', 'E'), ('C', 'F'), ('D', 'E'),
                  ('E', 'F'), ('E', 'H'), ('F', 'G'), ('I', 'J')])

T = nx.bfs_tree(G, 'A')
print(T.edges())
print(nx.shortest_path_length(G, 'A'))
```

---

## Distance Measure
### ==> Average distance (Average Shortest Path Length)
Average distance between every pair of nodes.
### ==> Diameter
Maximum distance between any pairs of nodes.
### ==> Eccentricity 
Maximum distance between a node n to all other nodes.
### ==> Radius
Minimum distance between any pairs of nodes.

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
                  ('B', 'K'), ('C', 'E'), ('C', 'F'), ('D', 'E'),
                  ('E', 'F'), ('E', 'H'), ('F', 'I'), ('I', 'J')])

### ==> Average distance (Average Shortest Path Length)
print(nx.average_shortest_path_length(G))
### ==> Diameter
print(nx.diameter(G))
### ==> Eccentricity
print(nx.eccentricity(G))
### ==> Radius
print(nx.radius(G))
```
