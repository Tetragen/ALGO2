'''
Functions used for the greedy matching algorithm
'''
from graphviz import Graph


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
    dot = Graph(engine="circo")
    # dot = Graph()
    for edge in edges_list:
        if edge not in matching:
            dot.edge(str(edge[0]), str(edge[1]),
                     color="darkolivegreen4", penwidth="1.1")
        else:
            dot.edge(str(edge[0]), str(edge[1]),
                     color='#4286f4',
                     penwidth='4')

    # visualize the graph
    graph_name = dir_name+"_circo/circo_greedy_"+str(index)
    # graph_name = dir_name+"/greedy_"+str(index)
    dot.attr(label=r"\nMatching size: {}\nAlgo step: {}\nNb nodes: {}".format(matching_length, index, len(nodes)),
             fontsize='30')
    dot.render(graph_name)


def match_graph(edges_list, nodes, dir_name):
    """
     apply greedy algorithm
    """
    print('\n======')
    print('greedy algorithm')
    print('======')
    matched_nodes = []
    matching = []
    index = 1
    for edge in edges_list:
        print('\n----')
        print(edge)
        if edge[0] in matched_nodes:
            print("node {} already matched".format(edge[0]))
        elif edge[1] in matched_nodes:
            print("node {} already matched".format(edge[1]))
        else:
            # add the nodes to the list of matched nodes
            matched_nodes += edge
            matching.append(edge)
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

    print("\n====\nfinal matching length : {}".format(matching_length))
    print("initial number of nodes : {}".format(len(nodes)))
    print("number of unmatched nodes : {}".format(
        len(nodes)-len(matched_nodes)))
    # quick text
    if len(matching)*2 == len(matched_nodes):
        print("number of matched nodes equals 2 times size of matching : ok")
    else:
        print("inconsistent number of edges in the matching and matched nodes")
