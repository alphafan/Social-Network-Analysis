### Edge Attributes in NetworkX

```python
import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=6, relation='family')
G.add_edge('B', 'C', weight=3, relation='friend')

# Get all edges
G.edges()
# Get all edges with all attribute values
G.edges(data=True)
# Get all edges with only specific attributes values
G.edges(data='relation')

# Get attributes of specific edge
attrs = G.edge['A']['B']
# Get specific attribute value of an edge
value = G.edge['A']['B']['relation']
```

---

### Access Edge Attributes in Multi Graph

```python
import networkx as nx

G = nx.MultiGraph()
G.add_edge('A', 'B', weight=6, relation='family')
G.add_edge('A', 'B', weight=1, relation='neighbor')
G.add_edge('B', 'C', weight=3, relation='friend')

data = G['A']['B']
# {0: {'relation': 'family', 'weight': 6}, 1: {'relation': 'neighbor', 'weight': 1}}
relation = G['A']['B'][0]['relation']
# family
```

---

### Node Attributes in NetworkX

```python
import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=6, relation='friend')
G.add_edge('B', 'C', weight=6, relation='co-worker')

G.add_node('A', role='manager')
G.add_node('B', role='trader')
G.add_node('C', role='analyst')

# Access node data in NetworkX
nodes = G.nodes()
data = G.nodes(data=True)
role = G.nodes(data='role')
```