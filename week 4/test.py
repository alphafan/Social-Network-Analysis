import networkx as nx

G = nx.Graph()

G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'),
                  ('C', 'E'), ('D', 'E'), ('D', 'G'), ('E', 'G'), ('F', 'G')])

for node in G.nodes():
    G[node]['community'] = 1
G['A']['community'] = 0


g = nx.DiGraph()
g.add_edges_from([('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'A'), ('D', 'C')])

print(list(nx.cn_soundarajan_hopcroft(G)))
