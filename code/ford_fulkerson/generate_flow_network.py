import pickle
import numpy as np
import os
from graphviz import Digraph

dot = Digraph(comment="Graph used to study the maximum flow problem",
              strict=True)
dot.graph_attr["rankdir"] = "LR"

"""
This time the graph is oriented
"""

if not os.path.exists("data/"):
    os.makedirs("data")
if not os.path.exists("images/"):
    os.makedirs("images")


def generate_flow_network(nb_nodes, nb_edges, capacity_max):
    """
    nb_nodes: number of inner nodes in the graph
    (without source and sink)

    some edges will link nodes to source and sink.
    other edges will link nodes to nodes.

    max_edges: maximum number of edges. There might be less edges
    in the final graph as we remove self loops.

    capacity_max: maximum capacity of each edge in the graph.
    """
    flow_network = "network_{}_nodes_edges_{}_capmax_{}".format(
        nb_nodes, nb_edges, capacity_max
    )

    """
    capacities of the network
    """
    # capacities beetwwen inner nodes
    # initialize them to 0
    inner_capacities = np.zeros((nb_nodes, nb_nodes))
    with dot.subgraph(name="cluster_inner nodes") as inner_nodes:
        inner_nodes.attr(label="inner nodes")
        for edge_index in range(nb_edges):
            # add an edge
            node_1 = np.random.randint(0, nb_nodes)
            node_2 = np.random.randint(0, nb_nodes)
            # without self loops
            if not node_1 == node_2:
                inner_capacities[node_1][node_2] = np.random.randint(0, capacity_max+1)
                if inner_capacities[node_1][node_2]:
                    print("link {} to {} with capacity {}.".format(
                        node_1,
                        node_2,
                        int(inner_capacities[node_1][node_2])))
                    # draw the edge
                    inner_nodes.edge(
                        str(node_1),
                        str(node_2),
                        color="darkolivegreen4",
                        penwidth=str(inner_capacities[node_1][node_2]),
                        label=str(int(inner_capacities[node_1][node_2])),
                    )

    # capacitites between nodes and source
    dot.node("Source", shape="doublecircle")
    source_capacities = np.random.randint(0, capacity_max+1, nb_nodes)
    with dot.subgraph(name="cluster_source") as source_subgraph:
        for node in range(nb_nodes):
            if source_capacities[node]:
                # check if node is connected to other nodes
                # in the graph
                # if sum(inner_capacities[node, :]):
                print("link source to {} with capacity {}.".format(
                    node, source_capacities[node]))
                # draw the edge
                source_subgraph.edge(
                    "Source",
                    str(node),
                    color="#4ea533",
                    penwidth=str(source_capacities[node]),
                    label=str(source_capacities[node]),
                )
    # capacitites between nodes and sink
    dot.node("Sink", shape="doublecircle")
    sink_capacities = np.random.randint(0, capacity_max+1, nb_nodes)
    with dot.subgraph(name="cluster_sink") as sink_subgraph:
        for node in range(nb_nodes):
            if sink_capacities[node]:
                # check if node is connected to other nodes in the graph
                # if sum(inner_capacities[:, node]):
                print("link {} to sink with capacity {}.".format(
                    node, sink_capacities[node]))
                # draw the edge
                sink_subgraph.edge(
                    str(node),
                    "Sink",
                    color="#4ea533",
                    penwidth=str(sink_capacities[node]),
                    label=str(sink_capacities[node]),
                )

    # visualize the graph
    dir_name = "images/" + flow_network
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    dot.attr(label=r"\nInitial Flow network",
             fontsize='20')
    dot.render(dir_name+"/initial_graph")

    # store data
    nodes = [x for x in range(1, nb_nodes + 1)]
    with open("data/" + flow_network + "_nodes", "wb") as f:
        pickle.dump(nodes, f)

    with open("data/" + flow_network + "_inner_capacities", "wb") as f:
        pickle.dump(inner_capacities, f)

    with open("data/" + flow_network + "_source_capacities", "wb") as f:
        pickle.dump(source_capacities, f)

    with open("data/" + flow_network + "_sink_capacities", "wb") as f:
        pickle.dump(sink_capacities, f)

    with open("data/" + flow_network + "_dot", "wb") as f:
        pickle.dump(dot, f)


generate_flow_network(10, 10, 2)
