"""
Load flow network and apply Ford Fulkerson
"""

import pickle
import ford_functions
import os
import ipdb
from graphviz import Graph


# number of nodes in the first group
nb_nodes_group_1 = 10
# number of nodes in the second group
nb_nodes_group_2 = 10
# number of edges
nb_edges = 15

flow_network = "network_{}_{}_nodes_edges_{}".format(
    nb_nodes_group_1, nb_nodes_group_2, nb_edges
)
dir_name = "images/" + flow_network

with open("data/" + flow_network + "_nodes_1", "rb") as f:
    nodes_1 = pickle.load(f)

with open("data/" + flow_network + "_nodes_2", "rb") as f:
    nodes_2 = pickle.load(f)

with open("data/" + flow_network + "_inner_capacities", "rb") as f:
    inner_capacities = pickle.load(f)

with open("data/" + flow_network + "_source_capacities", "rb") as f:
    source_capacities = pickle.load(f)

with open("data/" + flow_network + "_sink_capacities", "rb") as f:
    sink_capacities = pickle.load(f)

with open("data/" + flow_network + "_dot", "rb") as f:
    dot = pickle.load(f)

# apply Ford Fulkerson
ford_functions.apply_ford_fulkerson(
    nodes_1, nodes_2, inner_capacities, source_capacities, sink_capacities, dot, dir_name
)
# clean graphviz files
for filename in os.listdir(dir_name):
    if "pdf" not in filename:
        os.remove(dir_name + "/" + filename)
