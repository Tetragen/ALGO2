import pickle
import os
import random
from graphviz import Graph

dot = Graph(comment="Graph used to study the maximum matching problem")

"""
Generate graph data to perform the dominating set greedy
algorithm. We generate:
    - a dictionary of successors
    - a list of edges
"""
if not os.path.exists("data/"):
    os.makedirs("data")


def generate_graph(nb_nodes, max_nb_of_successors):
    """
    nb_nodes: number of inner nodes in the graph (meaning we don't take
    the sink and the source into account.
    max_nb_of_successors: maximum number of successors for a given node.
    """
    graph_name = "exercise_{}_nodes_max_{}_sccssrs".format(
        nb_nodes, max_nb_of_successors
    )
    successors = {}
    for node in range(1, nb_nodes + 1):
        nb_of_successors = random.randint(1, max_nb_of_successors)
        successors_of_node = random.sample(range(1, nb_nodes + 1), nb_of_successors)
        print(successors)
        # remove self-loops
        successors[node] = [
            vertex for vertex in successors_of_node if vertex is not node
        ]

    # print(successors)

    edges_list = []
    # build list of edges
    for node in range(1, nb_nodes + 1):
        for successor_of_node in successors[node]:
            print([node, successor_of_node])
            if [node, successor_of_node] not in edges_list:
                edges_list.append([node, successor_of_node])

    print(edges_list)
    print(len(edges_list))

    for edge in edges_list:
        dot.edge(str(edge[0]), str(edge[1]), color="darkolivegreen4", penwidth="1.1")

    nodes = [x for x in range(1, nb_nodes + 1)]
    with open("data/" + graph_name + "_nodes", "wb") as f:
        pickle.dump(nodes, f)

    with open("data/" + graph_name + "_successors", "wb") as f:
        pickle.dump(successors, f)

    with open("data/" + graph_name + "_edges", "wb") as f:
        pickle.dump(edges_list, f)

    # visualize the graph
    graph_name = "images/" + graph_name
    dot.render(graph_name)


generate_graph(50, 5)
generate_graph(10, 4)
