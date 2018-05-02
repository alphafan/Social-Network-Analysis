"""
Assignment 1 - Creating and Manipulating Graphs
Eight employees at a small company were asked to choose 3 movies that
they would most enjoy watching for the upcoming company movie night.
These choices are stored in the file Employee_Movie_Choices.txt.

A second file, Employee_Relationships.txt, has data on the relationships between different coworkers.

The relationship score has value of -100 (Enemies) to +100 (Best Friends).
A value of zero means the two employees haven't interacted or are indifferent.

Both files are tab delimited.
"""

import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite

# This is the set of employees
employees = {'Pablo', 'Lee', 'Georgia', 'Vincent', 'Andy', 'Frida', 'Joan', 'Claude'}

# This is the set of movies
movies = {'The Shawshank Redemption', 'Forrest Gump', 'The Matrix', 'Anaconda', 'The Social Network', 'The Godfather',
          'Monty Python and the Holy Grail', 'Snakes on a Plane', 'Kung Fu Panda', 'The Dark Knight', 'Mean Girls'}


# you can use the following function to plot graphs
# make sure to comment it out before submitting to the autograder
def plot_graph(graph, weight_name=None):
    """
    G: a NetworkX G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    """
    import matplotlib.pyplot as plt

    plt.figure()
    pos = nx.spring_layout(graph)
    edges = graph.edges()

    if weight_name:
        weights = [int(graph[u][v][weight_name]) for u, v in edges]
        labels = nx.get_edge_attributes(graph, weight_name)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        nx.draw_networkx(graph, pos, edges=edges, width=weights)
    else:
        nx.draw_networkx(graph, pos, edges=edges)


# ==> Question 1
# Using NetworkX, load in the bipartite graph from Employee_Movie_Choices.txt and return that graph.
# This function should return a NetworkX graph with 19 nodes and 24 edges

def answer_one():
    # Your Code Here
    graph = nx.read_edgelist('Employee_Movie_Choices.txt', create_using=nx.DiGraph(), delimiter='\t')
    return graph  # Your Answer Here


answer_one()
