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
    graph = nx.read_edgelist('Employee_Movie_Choices.txt', delimiter='\t')
    return graph  # Your Answer Here


# ==> Question 2
# Using the graph from the previous question, add nodes attributes named 'type' where movies have the value
# 'movie' and employees have the value 'employee' and return that graph.
# This function should return a networkx graph with node attributes {'type': 'movie'} or {'type': 'employee'}

def answer_two():
    # Your Code Here
    graph = answer_one()
    for employee in employees:
        graph.add_node(employee, type='employee')
    for movie in movies:
        graph.add_node(movie, type='movie')
    return graph  # Your Answer Here


# ==> Question 3
# Find a weighted projection of the graph from answer_two which tells us
# how many movies different pairs of employees have in common.
# This function should return a weighted projected graph.

def answer_three():
    # Your Code Here
    graph = answer_two()
    graph = bipartite.weighted_projected_graph(graph, employees)
    return graph  # Your Answer Here


# ==> Question 4
# Suppose you'd like to find out if people that have a high relationship score also like the same types of movies.
# Find the Pearson correlation ( using DataFrame.corr() ) between employee relationship scores and
# the number of movies they have in common. If two employees have no movies in common it should be
# treated as a 0, not a missing value, and should be included in the correlation calculation.
# This function should return a float.

def answer_four():
    # Your Code Here

    # Obtain Relation Score DF
    relation_score = nx.read_edgelist(path='Employee_Relationships.txt',
                                      data=[('relationship', int)],
                                      delimiter='\t')
    relation_df = pd.DataFrame(relation_score.edges(data=True), columns=['n1', 'n2', 'relationship'])
    relation_df['relationship'] = relation_df['relationship'].map(lambda x: x['relationship'])

    # Obtain Movies Choices DF
    movie_choice = nx.read_edgelist('Employee_Movie_Choices.txt', delimiter='\t')
    movie_choice = bipartite.weighted_projected_graph(movie_choice, employees)
    choice_df = pd.DataFrame(movie_choice.edges(data=True), columns=['n1', 'n2', 'common'])
    choice_df['common'] = choice_df['common'].map(lambda x: x['weight'])

    # Merge two data frame
    df = pd.merge(left=relation_df, right=choice_df, how='outer', on=['n1', 'n2'])
    df = df.fillna(0)

    # Get correlation
    return df.corr()['relationship']['common']  # Your Answer Here


answer_four()
