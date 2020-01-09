'''
Functions used for the greedy matching algorithm
'''
# from graphviz import Graph
import networkx as nx
import matplotlib.pyplot as plt


def show_matching(nodes,
                  edges_list,
                  matching,
                  index,
                  matching_length,
                  dir_name):
    """
    function to highlight the matching edges
    and save the graph image
    """
    G = nx.Graph()

    # set colors
    edge_colors = list()
    unmatched_edge_color="#1b50a1"
    matched_edge_color="#eb6b34"
    node_color="#b6cef2"

    # build the graph
    for edge in edges_list:
        G.add_edge(edge[0], edge[1])

    # we use sets because 
    # G.edges can change the indexing in the edges
    for edge in G.edges:
        if set(edge) in matching:
            edge_colors.append(matched_edge_color)
        else:
            edge_colors.append(unmatched_edge_color)

    # visualize the graph
    graph_name = dir_name+"greedy_"+str(index)+".pdf"
    graph_title=f"\nMatching size: {matching_length}\nAlgo step: {index}\nNb nodes: {len(nodes)}"

    plt.title(graph_title, fontsize=9)
    # we give a seed to the layout engine
    # in order to always have the same layout
    # fot a given  graph.
    # Otherwise, a random seed is used.
    pos=nx.spring_layout(G, seed=1)
    # if you want a circular layout
    # pos=nx.circular_layout(G)
    nx.draw(G,
            pos=pos,
            node_size=200,
            node_color=node_color,
            edge_color=edge_colors,
            font_size=8,
            width=1,
            with_labels=True)
    plt.tight_layout()
    plt.axis('off')
    plt.savefig(graph_name)
    plt.close()


def match_graph(edges_list, nodes, dir_name):
    """
     apply greedy algorithm
    """
    print('\n======')
    print('greedy algorithm')
    print('======')
    matched_nodes = list()
    matching = list()
    index = 1
    for edge in edges_list:
        print('\n----')
        print(edge)
        if edge[0] in matched_nodes:
            print(f"node {edge[0]} already matched")
        elif edge[1] in matched_nodes:
            print(f"node {edge[1]} already matched")
        else:
            # add the nodes to the list of matched nodes
            matched_nodes += edge
            matching.append(set(edge))
            print("add edge")
            print("matched_nodes")
            print(matched_nodes)
            print("matching")
            print(matching)
            # print("matching length")
            # print(len(matching))
            matching_length = len(matching)
            show_matching(nodes,
                          edges_list,
                          matching,
                          index,
                          matching_length,
                          dir_name)
        # increment algorithm index
        index += 1

    print(f"\n====\nfinal matching length : {matching_length}")
    print(f"initial number of nodes : {len(nodes)}")
    print(f"number of unmatched nodes : {len(nodes)-len(matched_nodes)}")
    # quick text
    if len(matching)*2 == len(matched_nodes):
        print("number of matched nodes equals 2 times size of matching : ok")
    else:
        print("inconsistent number of edges in the matching and matched nodes")
