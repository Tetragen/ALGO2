"""
   greedy algo to try to find a minimal dominant set
"""

import pickle
from graphviz import Graph
dot = Graph(comment='Graph used to study the dominating set problem')

with open('data/exercise_1_successors', 'rb') as f:
    successors = pickle.load(f)

with open('data/exercise_1_edges', 'rb') as f:
    edges_list = pickle.load(f)

# print(successors)
# size of the graph (number of edges)
n = len(successors)

"""
    sort the nodes by degree
    aka the number of successors
"""


sorted_dictionary = sorted(successors,
                           key=lambda node: len(successors[node]),
                           reverse=True)
# sorted does not modify the original sequence and returns a new dico
# it returns a list
# print(type(sorted_dictionary))

print('=====')
print('sorted dictionary of successors by degree of the node')
print('=====')


for node in sorted_dictionary:
    print('node  ' + str(node))
    print('successors ' + str(successors[node]))


"""
    prepare graph plot
"""

dot = Graph(comment='Graph 1 : dominating set')
for edge in edges_list:
    dot.edge(str(edge[0]),
             str(edge[1]),
             color='darkolivegreen4',
             penwidth='1.1')
graph_name = 'images/greedy_1_dominate/greedy_0'
dot.render(graph_name)


def highlight_node(node, dot, index):
    dot.node(str(node),
             color='forestgreen',
             penwidth='4')
    # visualize the graph
    graph_name = 'images/greedy_1_dominate/greedy_' + str(index)
    dot.render(graph_name)


"""
    greedy algorithm
"""

print('\n======')
print('greedy algorithm')
print('======')

not_dominated_nodes = [i for i in range(1, n + 1)]
growing_set = []


# use an index for plotting images
index = 0
for node in sorted_dictionary:
    # stop of the set is dominating
    index += 1
    if node in not_dominated_nodes:
        if len(not_dominated_nodes) > 0:
            # update our set
            growing_set.append(node)
            print('\nadd ' + str(node) + ' to the set')
            # update the list of not dominated nodes
            not_dominated_nodes.remove(node)
            print('remove ' + str(node) +
                  ' from the list of not dominated nodes')
            # print('successors : ')
            for successor in successors[node]:
                if successor in not_dominated_nodes:
                    # update the list of not dominated nodes
                    not_dominated_nodes.remove(successor)
                    print('remove ' + str(successor) +
                          ' from the list of not dominated nodes')
        # see how many more nodes we have to dominate
        print('still have to dominate ' +
              str(len(not_dominated_nodes)) + ' nodes')
        highlight_node(node, dot, index)
