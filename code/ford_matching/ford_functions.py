import ipdb
import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt


def apply_ford_fulkerson(
    nodes_1,
    nodes_2,
    inner_capacities,
    source_capacities,
    sink_capacities,
    G,
    pos,
    dir_name
):
    """
        Apply Ford Fulkerson algorithm.


        1) We first build a matrix containing all the capacities.
        ---------------------------------------------------------

        The capacities between the source and the inner nodes
        are contained on row 0.
        The capacities between inner nodes and the sink
        are contained on the last row.
        The capacities between inner nodes are contained between
        row 1 and row len(nodes)-1.

        2) We then perform the Ford Fulkerson algorithm
        -----------------------------------------------

        At each step of the algorithm, we do the following :

        --------
        a) Build the residual graph from the initial capacities and
        the current flow.
        - The function show_residual_network() plots the network.

        --------
        b) Look for augmenting paths in the residual graph.
        - The function find_augmenting_path() looks for augmenting paths
        by performing a DFS search in the graph.
        We could do better.
        - The function highlight_path() plots the chosen
        augmenting path.

        --------
        c) If we found an augmenting path, we modify the flow.
        - This is done in the function augment_flow()
        - The function check_flow() tests that the flow
        complies with the hypothesis of a flow network.
        - The function show_flow() plots the flow.

        d) Otherwise, we did not find an augmenting path.
        This means that our flow is optimal.
    """

    nodes = nodes_1+nodes_2
    # build a complete matrix of capacities
    capacities = np.zeros((len(nodes) + 2, len(nodes) + 2))
    # add capacities between source and inner nodes
    capacities[0, 1:-1] = source_capacities
    # add capacities between inner nodes and sink
    capacities[1:-1, -1] = sink_capacities
    # add capacities between inner nodes
    capacities[1: len(nodes) + 1, 1: len(nodes) + 1] = inner_capacities

    # initial flow set to 0
    # the total number of vertices in the graph
    # is len(nodes)+2 since we must take into account
    # the source and the sink.
    flow = np.zeros((len(nodes) + 2, len(nodes) + 2))

    # Algorithm iterations
    step = 1
    while True:
        print("===================\nAlgorithm step : {}".format(step))

        # compute the residual capacities
        residual_capacities = capacities-flow
        # print(flow)

        # show the residual network
        # it might have more edges since we changed the capacities
        G_residual = build_residual_graph(G,
                                          nodes_1,
                                          nodes_2,
                                          residual_capacities,
                                          capacities)
        show_residual_network_nx(G_residual, pos, residual_capacities,
                                 capacities, nodes_1, nodes_2, dir_name, step)

        # first look for possible augmenting paths
        augmenting_paths = find_augmenting_path(residual_capacities)
        if augmenting_paths:
            print("found augmenting paths in residual graph")
            # update the flow
            flow = augment_flow(flow,
                                residual_capacities,
                                augmenting_paths,
                                dir_name,
                                G_residual,
                                pos,
                                step,
                                nodes,
                                nodes_1,
                                nodes_2)
            residual_capacities = capacities-flow
            # print("new flow")
            # print(flow)

            # check if the flow matrix is really a flow
            check_flow(flow, nodes, capacities)

            # compute the value of the flow
            # it corresponds to what goes out of the source
            flow_value = sum(flow[0, :])
            print(f"flow value {flow_value}\n\n\n")

            # print the flow
            show_flow(flow, dir_name, step, flow_value, nodes_1, nodes_2)

            # update algo step
            step += 1
        else:
            print("\n=====================\n")
            print("found no augmenting path : flow is optimal")
            print("stopping at step {}".format(step))
            print("flow value: {}".format(flow_value))
            print("\n=====================\n")
            break


def show_flow(flow, dir_name, step, flow_value, nodes_1, nodes_2):

    # copy of the graph to edit the plot

    # we dont want node 1 to be the sink
    nodes = nodes_1+nodes_2
    for node_1 in range(len(nodes)+1):
        for node_2 in range(1, len(nodes)+2):
            if not node_1 == node_2:
                edge_flow = flow[node_1, node_2]
                if edge_flow > 0:
                    if node_1 == 0:
                        label_1 = "Source"
                        label_2 = "1- {}".format(node_2-1)
                    elif node_2 == len(nodes)+1:
                        label_1 = "2- {}".format(node_1-1)
                        label_2 = "Sink"
                    else:
                        if node_1 < node_2:
                            label_1 = "1- {}".format(node_1-1)
                            label_2 = "2- {}".format(node_2-1)
                        elif node_2 < node_1:
                            label_1 = "2- {}".format(node_1-1)
                            label_2 = "1- {}".format(node_2-1)


def show_residual_network_nx(G_residual, pos, residual_capacities, capacities, nodes_1,
                             nodes_2,
                             dir_name, step):

    edges_width = list()
    edges_colors = list()

    for edge in G_residual.edges:
        reverse = False
        if edge[0] == "Source":
            node_group_1 = int(edge[1].split('-')[1])
            residual_capacity = residual_capacities[0, node_group_1+1]
        elif edge[0] == "Sink":
            reverse = True
            node_group_2 = int(edge[1].split('-')[1])
            residual_capacity = residual_capacities[-1, node_group_2+1]
        elif edge[1] == "Sink":
            node_group_2 = int(edge[0].split('-')[1])
            residual_capacity = residual_capacities[node_group_2+1, -1]
        elif edge[1] == "Source":
            reverse = True
            node_group_1 = int(edge[0].split('-')[1])
            residual_capacity = residual_capacities[node_group_1+1, 0]
        elif edge[0].split('-')[0] == "2":
            reverse = True
            node_group_2 = int(edge[0].split('-')[1])
            node_group_1 = int(edge[1].split('-')[1])
            residual_capacity = residual_capacities[node_group_2 +
                                                    1, node_group_1+1]
        else:
            node_group_1 = int(edge[0].split('-')[1])
            node_group_2 = int(edge[1].split('-')[1])
            residual_capacity = residual_capacities[node_group_1 +
                                                    1, node_group_2+1]
        if residual_capacity != 0:
            if reverse:
                edges_width.append(1)
                edges_colors.append("#67d627")
            else:
                edges_width.append(1)
                edges_colors.append("#f5b342")
        else:
            edges_width.append(0.01)
            edges_colors.append("#1b50a1")

    node_color = "#b6cef2"
    plt.title(f"residual graph step {step}")
    nx.draw(G_residual,
            pos,
            node_size=160,
            node_color=node_color,
            font_size=6,
            edge_color=edges_colors,
            width=edges_width,
            with_labels=True)
    # plt.tight_layout()
    plt.savefig(dir_name+f"/step_{step}__residual.pdf")
    plt.close()


def check_flow(flow, nodes, capacities):
    """
        Check if the flow complies with the constraints
        of a flow network
    """
    print("---\nchecking flow")
    inner_flow = flow[1:-1, 1:-1]

    # -------------
    # First check
    # -------------
    # check if for all nodes u and v,
    # that are different from the source,
    # and different from the sink, we have
    # f(u,v)=-f(v,u)
    # We can do it using matrices
    antisymmetry_check = np.transpose(inner_flow) == -inner_flow
    flow_check_1 = antisymmetry_check.all()
    if flow_check_1:
        print("First check ok : flow matrix is symmetric.")
    else:
        print("Flow not ok ! Not symmetrical.")

    # -------------
    # Second check
    # -------------
    # test that what goes out of a node
    # is the same as what comes in,
    # for any node different from the sink
    # and the difference from the source.
    flow_check_2 = []
    for node in range(1, len(nodes) + 1):
        flow_check_2.append(sum(flow[:, node]) == sum(flow[node, :]))
    if all(flow_check_2):
        print("Second check ok : output of nodes are the same as inputs.")
    else:
        print("Flow not ok ! One node outputs a quantity not equal to its input.")

    # -------------
    # Third check
    # -------------
    # test that the flow on each edge does node exceed
    # the capacity of the edge
    comparison = flow <= capacities
    flow_check_3 = comparison.all()
    if flow_check_3:
        print("Third check ok : flow does not exceed capacity on each edge.")
    else:
        print("Flow not ok ! The flow on one edge exceeds its capacity.")

#    # -------------
#    # Fourth check
#    # -------------
#    # the flow must be positive
#    comparison_4 = flow >= 0
#    flow_check_4 = comparison_4.all()
#    if flow_check_4:
#        print("Fourth check ok : flow is positive.")
#    else:
#        print("Flow not ok ! The flow is not positive.")
    print("---\n")


def augment_flow(flow, residual_capacities, augmenting_paths, dir_name,
                 G_residual,
                 pos, step, nodes, nodes_1, nodes_2):
    print("---\naugment flow")

    # -----------
    # first choose an augmenting path randomly
    # from the ones we found.
    # or take the last one ? up to you
    augmenting_path = augmenting_paths.pop()
    print(f"chosen augmenting path : {augmenting_path}")

    # compute the capacity of this path.
    # We take the capacities from the source to the sink
    # without the sink.
    augmenting_path_capacities = []
    for node_index in range(len(augmenting_path)-1):
        node_1 = augmenting_path[node_index]
        node_2 = augmenting_path[node_index+1]
        # print(node_1)
        # print(node_2)
        augmenting_path_capacities.append(residual_capacities[node_1][node_2])
    # The capacit of a path is the minimum of the capacities
    # of each edge.
    path_capacity = min(augmenting_path_capacities)
    print(f"augmenting path capacity : {path_capacity}")

    # highlight this path in the graph
    highlight_path(G_residual, pos, augmenting_path, dir_name, step,
                   nodes, nodes_1, nodes_2, path_capacity)

    # -----
    # finally augment the flow
    nb_nodes = len(nodes)+2
    added_flow_value = path_capacity
    added_flow = np.zeros((nb_nodes, nb_nodes))
    for node_index in range(len(augmenting_path)-1):
        node_1 = augmenting_path[node_index]
        node_2 = augmenting_path[node_index+1]
        added_flow[node_1, node_2] = added_flow_value
        added_flow[node_2, node_1] = -added_flow_value
    return flow + added_flow


def find_augmenting_path(residual_capacities):
    """
        Look for an augmenting path in the residual graph by
        depth-first search (DFS)
    """
    # we want to go from the source to the sink
    # using edges in the residual graph
    last_index = residual_capacities.shape[1]-1
    print("---\nLook for augmenting paths in the residual graph")
    print("source = 0")
    print(f"sink = {last_index}")
    print("---")
    augmenting_paths = []
    stack = [(0, [0])]
    while stack:
        (vertex, path) = stack.pop()
        # careful, we put all the capacities in a single matrix
        # thus :
        # source is on rank 0
        # node 0 is on rank 1
        # node 1 is on rank 2
        # node 2 is on rank 3
        # node len(nodes) -1 is on rank len(nodes)
        # sink is on rank len(nodes)+1
        next_available_nodes = np.where(residual_capacities[vertex,
                                                            :])[0]
        for next_node in next_available_nodes:
            # print("next node {}".format(next_node))
            if next_node == last_index:
                print(f"found augmenting path : {path+[next_node]}")
                # avoid loops !
                if next_node not in path:
                    augmenting_paths.append(path+[next_node])
            else:
                # avoid loops !
                if next_node not in path:
                    stack.append((next_node, path+[next_node]))
    return augmenting_paths


def highlight_path(G_residual,
                   pos,
                   augmenting_path,
                   dir_name,
                   step,
                   nodes,
                   nodes_1,
                   nodes_2,
                   path_capacity):
    print(f"highlight path {augmenting_path}")

    # reformat augmenting path
    augmenting_path_edges = list()
    for index in range(len(augmenting_path)-1):
        augmenting_path_edges.append(
            [augmenting_path[index], augmenting_path[index+1]])

    edges_width = list()
    edges_colors = list()
    for edge in G_residual.edges:
        if edge[0] == "Source":
            node_group_1 = int(edge[1].split('-')[1])
            parsed_edge = [0, node_group_1+1]
        elif edge[0] == "Sink":
            node_group_2 = int(edge[1].split('-')[1])
            parsed_edge = [len(nodes)+1, node_group_2+1]
        elif edge[1] == "Sink":
            node_group_2 = int(edge[0].split('-')[1])
            parsed_edge = [node_group_2+1, len(nodes)+1]
        elif edge[1] == "Source":
            node_group_1 = int(edge[0].split('-')[1])
            parsed_edge = [node_group_1, 0]
        elif edge[0].split('-')[0] == "2":
            node_group_2 = int(edge[0].split('-')[1])
            node_group_1 = int(edge[1].split('-')[1])
            parsed_edge = [node_group_2+1, node_group_1+1]
        else:
            node_group_1 = int(edge[0].split('-')[1])
            node_group_2 = int(edge[1].split('-')[1])
            parsed_edge = [node_group_1+1, node_group_2+1]
        if parsed_edge in augmenting_path_edges:
            edges_width.append(1)
            edges_colors.append("#d627c2")
        else:
            edges_width.append(0.01)
            edges_colors.append("#1b50a1")

    node_color = "#b6cef2"
    plt.title(f"augmenting path step {step}")
    nx.draw(G_residual,
            pos,
            node_size=160,
            node_color=node_color,
            font_size=6,
            edge_color=edges_colors,
            width=edges_width,
            with_labels=True)
    plt.savefig(dir_name+f"/step_{step}_augmenting.pdf")
    plt.close()


def build_residual_graph(G,
                         nodes_1,
                         nodes_2,
                         residual_capacities,
                         capacities):
    G_residual = G.copy()
    nodes = nodes_1+nodes_2
    for node_1 in range(len(nodes)+2):
        for node_2 in range(len(nodes)+2):
            if not node_1 == node_2:
                residual_capacity = residual_capacities[node_1, node_2]
                initial_capacity = capacities[node_1, node_2]
                if node_1 == 0:
                    label_1 = "Source"
                    label_2 = f"1-{node_2-1}"
                elif node_1 == len(nodes)+1:
                    label_1 = "Sink"
                    label_2 = f"2-{node_2-1}"
                elif node_2 == 0:
                    label_1 = f"1-{node_1-1}"
                    label_2 = "Source"
                elif node_2 == len(nodes)+1:
                    label_1 = f"2-{node_1-1}"
                    label_2 = "Sink"
                else:
                    if node_1 < node_2:
                        label_1 = f"1-{node_1-1}"
                        label_2 = f"2-{node_2-1}"
                    elif node_2 < node_1:
                        label_1 = f"2-{node_1-1}"
                        label_2 = f"1-{node_2-1}"

                # process
                edge=(label_1, label_2)
                if residual_capacity == 0:
                    if edge in G_residual.edges:
                        G_residual.remove_edge(label_1, label_2)
                if residual_capacity != 0:
                    if initial_capacity == 0:
                        G_residual.add_edge(label_1, label_2)

    return G_residual
