import networkx as nx

graph = nx.karate_club_graph()
graph = nx.convert_node_labels_to_integers(graph, first_label=1)
degCent = nx.degree_centrality(graph)
print(degCent[34])
print(degCent[33])

G = nx.DiGraph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
                  ('B', 'K'), ('C', 'E'), ('C', 'F'), ('D', 'E'),
                  ('E', 'F'), ('E', 'H'), ('F', 'G'), ('I', 'J')])

degCent = nx.in_degree_centrality(G)
print(degCent)
degCent = nx.out_degree_centrality(G)
print(degCent)