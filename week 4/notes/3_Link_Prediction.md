In the past two videos, we looked at different models of network evolution. 
That given the dynamics for how a network evolves from the beginning to the end. 
Today we're going to look at a related problem which is given a fixed network, 
can we predict how this network is going to look in the future. And more 
specifically, we're going to be looking at the link prediction problem. 
Which is given a network, can we predict which edges are going to be formed 
in the future? This problem has a lot of applications, for example if you're 
Facebook and you want to create a friend recommendation algorithm or a friend 
recommender to tell people who they should friend. Then, basically you're solving 
this problem. You're looking at the current Facebook network and you're trying to 
predict which new friendships are likely to form in the future. Let's take this 
small network as an example and let's try to ask the question, what new edges are 
like.

## Link Prediction

__==> Q:__ What are the nodes that tends to be connected?

### Number of common neighbors that two nodes have.

```python
import networkx as nx

G = nx.karate_club_graph()
comm_neigh = [(e[0], e[1], len(list(nx.common_neighbors(G, e[0], e[1])))) for e in nx.non_edges(G)]

print(sorted(comm_neigh, key=lambda x: x[2], reverse=True))
```

### Jaccard Coefficient

```python
import networkx as nx

G = nx.karate_club_graph()

print(sorted(nx.jaccard_coefficient(G), key=lambda x: x[2], reverse=True))
```

### Resource Allocation Index

```python
import networkx as nx

G = nx.karate_club_graph()

print(sorted(nx.resource_allocation_index(G), key=lambda x: x[2], reverse=True))
```

### Adamic-Adar Index

```python
import networkx as nx

G = nx.karate_club_graph()

print(sorted(nx.adamic_adar_index(G), key=lambda x: x[2], reverse=True))
```

### Preferential Attachment 

Node with high degree trends to get more neighbors

```python
import networkx as nx

G = nx.karate_club_graph()

print(sorted(nx.preferential_attachment(G), key=lambda x: x[2], reverse=True))
```

### Community Common Neighbors

```python
import networkx as nx

G = nx.Graph()

G.add_edges_from([('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'D'), ('G', 'C'),
                  ('D', 'E'), ('D', 'G'), ('D', 'H'), ('E', 'H'), ('F', 'H')])

G.node['A']['community'] = 0
G.node['B']['community'] = 0
G.node['C']['community'] = 0
G.node['D']['community'] = 0
G.node['E']['community'] = 1
G.node['F']['community'] = 1
G.node['G']['community'] = 0
G.node['H']['community'] = 1

print(list(nx.cn_soundarajan_hopcroft(G)))
```

### Community Resource Allocation Index

```python
import networkx as nx

G = nx.Graph()

G.add_edges_from([('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'D'), ('G', 'C'),
                  ('D', 'E'), ('D', 'G'), ('D', 'H'), ('E', 'H'), ('F', 'H')])

G.node['A']['community'] = 0
G.node['B']['community'] = 0
G.node['C']['community'] = 0
G.node['D']['community'] = 0
G.node['E']['community'] = 1
G.node['F']['community'] = 1
G.node['G']['community'] = 0
G.node['H']['community'] = 1

print(list(nx.ra_index_soundarajan_hopcroft(G)))
```

