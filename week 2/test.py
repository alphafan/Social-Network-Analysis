import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
                  ('B', 'K'), ('C', 'E'), ('C', 'F'), ('D', 'E'),
                  ('E', 'F'), ('E', 'H'), ('F', 'I'), ('I', 'J')])

print(nx.edge_connectivity(G, 'A', 'H'))
# 1
print(nx.minimum_edge_cut(G, 'A', 'H'))