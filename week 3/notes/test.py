import networkx as nx

graph = nx.karate_club_graph()
graph = nx.convert_node_labels_to_integers(graph, first_label=1)
degCent = nx.degree_centrality(graph)
print(degCent[34])
print(degCent[33])