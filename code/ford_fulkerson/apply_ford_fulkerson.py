"""
Load flow network and apply Ford Fulkerson
"""

import pickle
import ford_functions
import os
import ipdb
from graphviz import Graph


def apply_algorithm(nb_nodes, nb_edges, capacity_max):
    flow_network = f"network_{nb_nodes}_nodes_edges_{nb_edges}_capmax_{capacity_max}"
    dir_name = "images/" + flow_network+"/"

    with open("data/" + flow_network + "_nodes", "rb") as f:
        nodes = pickle.load(f)

    with open("data/" + flow_network + "_inner_capacities", "rb") as f:
        inner_capacities = pickle.load(f)

    with open("data/" + flow_network + "_source_capacities", "rb") as f:
        source_capacities = pickle.load(f)

    with open("data/" + flow_network + "_sink_capacities", "rb") as f:
        sink_capacities = pickle.load(f)

    with open("data/" + flow_network + "_G", "rb") as f:
        G = pickle.load(f)

    with open("data/" + flow_network + "_pos", "rb") as f:
        pos = pickle.load(f)

    # create directory of necessary
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    # clean directory
    for image in os.listdir(dir_name):
        if "initial" not in image:
            os.remove(dir_name+image)

    # apply Ford Fulkerson
    ford_functions.apply_ford_fulkerson(
        nodes, inner_capacities, source_capacities, sink_capacities,
        dir_name, G, pos
    )


apply_algorithm(25, 25, 2)
