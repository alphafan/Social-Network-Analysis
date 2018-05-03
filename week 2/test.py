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