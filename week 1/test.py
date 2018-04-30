from networkx.algorithms import bipartite
import networkx as nx

B = nx.Graph()
B.add_nodes_from(['A', 'B', 'C', 'D', 'E'], bipartite=0)
B.add_nodes_from(['1', '2', '3', '4', '5'], bipartite=1)
B.add_edges_from([('A', '1'), ('B', '1'), ('C', '1'),
                  ('C', '3'), ('D', '2'), ('E', '3'),
                  ('E', '4'), ('E', '5')])

a = bipartite.is_bipartite(B)
# True
B.add_edge('A', 'B')
b = bipartite.is_bipartite(B)
# False

print(a, b)
