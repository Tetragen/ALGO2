""" greedy algo to try to find a minimal dominant set
"""

import pickle
import matching_functions
import os
import networkx as nx
import matplotlib.pyplot as plt


def match_graph(nb_nodes: int, max_nb_of_successors: int):
    graph_name = f"n={nb_nodes}_maxs={max_nb_of_successors}"

    with open(f"data/{graph_name}_nodes", "rb") as f:
        nodes = pickle.load(f)

    with open(f"data/{graph_name}_edges", "rb") as f:
        edges_list = pickle.load(f)

    dir_name = f"images/{graph_name}/"

    # create directory of necessary
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # clean directory
    for image in os.listdir(dir_name):
        if "initial" not in image:
            os.remove(dir_name+image)

    # apply greedy algorithm
    matching_functions.match_graph(edges_list, nodes, dir_name)

match_graph(20, 3)
