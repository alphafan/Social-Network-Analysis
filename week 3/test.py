import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'B'),
                  ('B', 'D'),
                  ('A', 'C'),
                  ('C', 'D'),
                  ('C', 'E'),
                  ('D', 'E'),
                  ('E', 'G'),
                  ('D', 'G'),
                  ('G', 'F')
                  ])

print(nx.edge_betweenness_centrality(G, normalized=False))