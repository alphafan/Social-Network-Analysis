## Load a Graph

```python
import networkx as nx
import numpy as np
import pandas as pd


# ==> Method 1: Create graph by adding node/edges pairs
# Instantiate the graph
G1 = nx.Graph()
# add node/edge pairs
G1.add_edges_from([(0, 1),
                   (0, 2),
                   (0, 3),
                   (0, 5),
                   (1, 3),
                   (1, 6),
                   (3, 4),
                   (4, 5),
                   (4, 7),
                   (5, 8),
                   (8, 9)])


# ==> Method 2: Load from adjacent list file
G2 = nx.read_adjlist('G_adjlist.txt', nodetype=int)


# ==> Method 3: Read from adjacent matrix
G_mat = np.array([[0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
G3 = nx.Graph(G_mat)


# ==> Method 4: Load from edge list file
G4 = nx.read_edgelist('G_edgelist.txt', data=[('Weight', int)])


# ==> Method 5: Read from pandas data frame
G_df = pd.read_csv('G_edgelist.txt', delim_whitespace=True,
                   header=None, names=['n1', 'n2', 'weight'])
G5 = nx.from_pandas_edgelist(G_df, 'n1', 'n2', edge_attr='weight')

```