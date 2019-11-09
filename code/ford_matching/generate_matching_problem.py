import pickle
import numpy as np
import os
from graphviz import Digraph

dot = Digraph(comment="Applying the Ford Fulkerson algorithm to a matching problem",
              strict=True)
dot.graph_attr["rankdir"] = "LR"

"""
This time the graph is oriented
"""

if not os.path.exists("data/"):
    os.makedirs("data")
if not os.path.exists("images/"):
    os.makedirs("images")


def generate_matching_problem(nb_nodes_group_1, nb_nodes_group_2, nb_edges):
    """
    nb_nodes: number of inner nodes in the graph (meaning we don't take
    the sink and the source into account.

    max_edges: maximum number of edges. There might be less edges
    in the final graph as we remove self loops.
    """
    flow_network = "network_{}_{}_nodes_edges_{}".format(
        nb_nodes_group_1, nb_nodes_group_2, nb_edges
    )

    # capacities of the network
    # capacities beetwwen inner nodes
    # initialize them to 0
    inner_capacities = np.zeros((nb_nodes_group_1+nb_nodes_group_2,
                                 nb_nodes_group_1+nb_nodes_group_2))

    with dot.subgraph(name="cluster_group 1") as group_1:
        group_1.attr(label=r"-------------------------------")
        for node in range(nb_nodes_group_1):
            group_1.node("1- {}".format(node))

    with dot.subgraph(name="cluster_group 2") as group_2:
        group_2.attr(label=r"-------------------------------")
        for node in range(nb_nodes_group_1, nb_nodes_group_1+nb_nodes_group_2):
            group_2.node("2- {}".format(node))

    # compatibilities between nodes
    for edge in range(nb_edges):
        node_1 = np.random.randint(0, nb_nodes_group_1)
        node_2 = np.random.randint(
            nb_nodes_group_1, nb_nodes_group_1 + nb_nodes_group_2)
        inner_capacities[node_1][node_2] = 1
        dot.edge("1- {}".format(node_1),
                 "2- {}".format(node_2),
                 penwidth="2",
                 color="darkolivegreen4")

    # introduce the source
    dot.node("Source", shape="doublecircle")
    source_group_1_capacities = np.ones(nb_nodes_group_1)
    source_group_2_capacitires = np.zeros(nb_nodes_group_2)
    source_capacities = np.concatenate((source_group_1_capacities,
                                        source_group_2_capacitires))
    for node in range(nb_nodes_group_1):
        dot.edge("Source",
                 "1- {}".format(node),
                 color="#4ea533")

    # introduce the sink
    dot.node("Sink", shape="doublecircle")
    sink_group_2_capacities = np.ones(nb_nodes_group_2)
    sink_group_1_capacities = np.zeros(nb_nodes_group_1)
    sink_capacities = np.concatenate(
        (sink_group_1_capacities, sink_group_2_capacities))
    for node in range(nb_nodes_group_1, nb_nodes_group_1+nb_nodes_group_2):
        dot.edge("2- {}".format(node),
                 "Sink",
                 color="#4ea533")

    # visualize the graph
    dir_name = "images/" + flow_network
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    dot.attr(label=r"\nInitial Flow network",
             fontsize='20')
    dot.render(dir_name+"/initial_graph")

    # store data
    nodes_1 = [x for x in range(1, nb_nodes_group_1 + 1)]
    with open("data/" + flow_network + "_nodes_1", "wb") as f:
        pickle.dump(nodes_1, f)

    nodes_2 = [x for x in range(
        nb_nodes_group_1, nb_nodes_group_1 + nb_nodes_group_2)]
    with open("data/" + flow_network + "_nodes_2", "wb") as f:
        pickle.dump(nodes_2, f)

    with open("data/" + flow_network + "_inner_capacities", "wb") as f:
        pickle.dump(inner_capacities, f)

    with open("data/" + flow_network + "_source_capacities", "wb") as f:
        pickle.dump(source_capacities, f)

    with open("data/" + flow_network + "_sink_capacities", "wb") as f:
        pickle.dump(sink_capacities, f)

    with open("data/" + flow_network + "_dot", "wb") as f:
        pickle.dump(dot, f)


generate_matching_problem(10, 10, 15)
