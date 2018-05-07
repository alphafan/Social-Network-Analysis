## Betweenness Centrality
What are the nodes that appear in the shortest path nodes in a graph?

<img src='../images/21.png' />

Question: whether or not include endpoint node.
 
 <img src='../images/22.png' />
 
 __==> Q:__ What if nodes can not reach all the other nodes?
 
 __==> A:__ Consider the nodes where there is at least one path that pass it.
 
 Larger graph tends to have larger centrality, so we will normalize them 
 by dividing by the size of graph
 
 ```python
import networkx as nx
import operator

graph = nx.karate_club_graph()
graph = nx.convert_node_labels_to_integers(graph, first_label=1)
btwnCent = nx.betweenness_centrality(graph, normalized=True, endpoints=False)

print(sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[:5])
```

---

__==> Q:__ Complexity of betweenness centrality?

__==> A:__ O ( n3 ). Very Expensive.

__==> Solution:__ 
- Approximation, compute based on a __sample__ of node.

 ```python
import networkx as nx
import operator

graph = nx.karate_club_graph()
graph = nx.convert_node_labels_to_integers(graph, first_label=1)
btwnCent = nx.betweenness_centrality(graph, normalized=True, endpoints=False, k=10)

print(sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[:5])
```

--- 

### Betweenness centrality between two groups

```python
import networkx as nx
import operator

graph = nx.karate_club_graph()
graph = nx.convert_node_labels_to_integers(graph, first_label=1)
btwnCent = nx.betweenness_centrality_subset(graph, sources=[34, 33, 21, 30, 16, 27, 15, 23, 10],
                                            targets=[1, 4, 13, 11, 6, 12, 17, 7], normalized=True)

print(sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[:5])
```

---

### Betweenness centrality to find important edges

```python
import networkx as nx
import operator

graph = nx.karate_club_graph()
graph = nx.convert_node_labels_to_integers(graph, first_label=1)
btwnCent = nx.edge_betweenness_centrality(graph)

print(sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[:5])
```

```python
import networkx as nx
import operator

graph = nx.karate_club_graph()
graph = nx.convert_node_labels_to_integers(graph, first_label=1)
btwnCent = nx.edge_betweenness_centrality_subset(graph, sources=[34, 33, 21, 30, 16, 27, 15, 23, 10],
                                                 targets=[1, 4, 13, 11, 6, 12, 17, 7], normalized=True)

print(sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[:5])
```