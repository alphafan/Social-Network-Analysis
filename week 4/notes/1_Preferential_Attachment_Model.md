## Degree Distribution

整个网络中 Degree 的分布情况。

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
degrees = G.degree()
degree_values = sorted(set(degrees.values()))
histogram = [list(degrees.values()).count(i) / float(nx.number_of_nodes(G)) for i in degree_values]

plt.bar(degree_values, histogram)
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()
```

## Degree Distribution in Real World

<img src='../images/8.png' />

绝大多数的节点的 degree 很少，很少数的节点的 degree 很大，分布的占比类似于一个倒指数分布。

## 如何解释这种行为？

Preferential Attachment Model. 可以想象，一个经常和其他演员合作的演员，会有更大的概率和新演员合作。

每个新节点可以根据定义加到 n 个已经存在的节点上，n 可以大于 1