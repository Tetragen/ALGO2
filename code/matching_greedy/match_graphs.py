""" greedy algo to try to find a minimal dominant set
"""

import pickle
import matching_functions
import os

# import ipdb
from graphviz import Graph

dot = Graph(comment="Graph used to study the matching set problem")

# number of nodes
nb_nodes = 50
# max_number_of_successors
max_nb_of_successors = 5

graph_name = f"n={nb_nodes}_maxs={max_nb_of_successors}"

with open("data/" + graph_name + "_nodes", "rb") as f:
    nodes = pickle.load(f)

with open("data/" + graph_name + "_edges", "rb") as f:
    edges_list = pickle.load(f)


# draw initial graph
dot = Graph(comment="Graph 1 : matching set")
for edge in edges_list:
    dot.edge(str(edge[0]), str(edge[1]),
             color="darkolivegreen4", penwidth="1.1")
dir_name = "images/" + graph_name+"_processed"

if not os.path.exists(dir_name):
    os.makedirs(dir_name)
dot.render("images/"+graph_name)

# apply greedy algorithm
matching_functions.match_graph(edges_list, nodes, dir_name)

# clean graphviz files
for filename in os.listdir(dir_name):
    if "pdf" not in filename:
        # print(filename)
        os.remove(dir_name + "/" + filename)
