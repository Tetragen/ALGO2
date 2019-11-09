"""
Load flow network and apply Ford Fulkerson
"""

import pickle
import ford_functions
import os
import ipdb
from graphviz import Graph


# number of nodes
nb_nodes = 10
# number of edges in the inner graph
nb_edges = 10
# maximum initial capacity of an edge
capacity_max = 2

flow_network = "network_{}_nodes_edges_{}_capmax_{}".format(
    nb_nodes, nb_edges, capacity_max
)
dir_name = "images/" + flow_network

with open("data/" + flow_network + "_nodes", "rb") as f:
    nodes = pickle.load(f)

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
    nodes, inner_capacities, source_capacities, sink_capacities, dot, dir_name
)
# clean graphviz files
for filename in os.listdir(dir_name):
    if "pdf" not in filename:
        os.remove(dir_name + "/" + filename)
