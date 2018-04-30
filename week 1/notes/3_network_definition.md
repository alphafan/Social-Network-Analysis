### Symmetric Graph (Un-directed Graph)
i.e. A is a friend of B -> B is a friend of A.
 
 ```python
import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
```

---

### Asymmetric Graph (Directed graph)
i.e. Animal A eats B -> Animal B does not eat A
 
 ```python
import networkx as nx

G = nx.DiGraph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')
```

---

### Weighted Network
Not all relationships are legal. Some edges can carry 
more weights than others.

 ```python
import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=6)
G.add_edge('B', 'C', weight=3)
```

---

### Signed Network
A network where edges are assigned positive or negative.

 ```python
import networkx as nx

G = nx.DiGraph()
G.add_edge('A', 'B', sign='+')
G.add_edge('B', 'C', sign='-')
```

---

### Other Attributes of Edges

 ```python
import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', relation='friend')
G.add_edge('B', 'C', relation='neighbor')
G.add_edge('C', 'D', relation='coworker')
G.add_edge('D', 'E', relation='family')
```

---

### Multi Graph
Multiple edges can connect the same nodes. Pair of nodes can 
have different types of relationships.

A is 'friend' of B. A is also 'neighbor' of B.

 ```python
import networkx as nx

G = nx.MultiGraph()
G.add_edge('A', 'B', relation='friend')
G.add_edge('A', 'B', relation='neighbor')
```
