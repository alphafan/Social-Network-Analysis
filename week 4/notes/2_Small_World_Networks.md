## Milgram Small World Experiment 

Set up (1960s): 
- 296 randomly chosen "starters" asked to forward a letter to a "target" person. 
- Target was a stockbroker in Boston. 
- Instructions for starter: 
    - Send letter to target if you know him on a first name basis. 
    - If you do not know target, send letter (and instructions) to someone you know on a first name basis who is more likely to know the target. 
- Some information about the target, such as city, and occupation, was provided. 

结果：
- 大部分是能送达的，64 / 296 被送达了，path length 大约是6，分布从 0 到 11 不等
- 人们是有能力找到最短路径的

## Microsoft Instance Message
- 240 active users
- Medium length is 7

## Facebook data
- 2008: 5.28 --> 2011: 4.74
- Even shorter if restricted in US

---

## Local Cluster Coefficient

- Degree 高的 node 一般 Local Cluster Coefficient 比较低
- 社交网络上平均 Local Cluster Coefficient 都比较高，说明人之间的连接是有自己的一套方案的， 
foaf 也是很正常的事情，为什么这个很高，因为如果我们对比完全随机生成的网络的话，他们的聚类系数
会很低很低的

## A model for these two properties?

- Short average path length
- High LCC

如果我们用之前的 Preferential Attachment Model 来生成这样的模型？

- 它确实能保证 Short average path length，原因是加入一个新节点的时候，会更倾向于连接到 degree 
比较大的节点，所以实际上是能保证很短的最短路径长度的
- 但是无法保证 High LCC

## Small World Model

给定 k 和重新连接的概率 p，在一定概率的情况下重新连接到一个随机的节点上去。

随着 p 的从小变到大，distance 和 LCC 都会变小

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.watts_strogatz_graph(1000, 6, 0.04)
degrees = G.degree()
degree_values = sorted(set(degrees.values()))
histogram = [list(degrees.values()).count(i) / float(nx.number_of_nodes(G)) for i in degree_values]

plt.bar(degree_values, histogram)
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()
```

## Small World Model in NetworkX
- connected_watts_strogatz_graph: 尝试 t 次，使得网络一定是连接的
- newman_watts_strogatz_graph: 不是rewire，而是加上一个新的连接



