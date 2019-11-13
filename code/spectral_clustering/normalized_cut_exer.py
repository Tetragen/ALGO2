"""
    We will study a heursitic for obtaining a relevant number of clusters
    in a clustering situation.
    The clustering will be performed by a Spectral Clustering.
    Spectral Clustering works with an adjacency matrix
    or a similarity matrix.
"""

from sklearn.cluster import SpectralClustering
import numpy as np
import matplotlib.pyplot as plt
import ipdb

# load the data
adjacency_matrix = np.load("data/adjacency_matrix.npy")
# nb datapoints
nb_datapoints = adjacency_matrix.shape[0]
dataset = [x for x in range(nb_datapoints)]


def cluster_and_compute_normalized_cut(nb_clusters, adjacency_matrix):
    sc = SpectralClustering(nb_clusters, affinity='precomputed')
    # n_init=100)
    # assign_labels='discretize')

    # apply the Spectral Clustering to the adjacency matrix
    sc.fit_predict(adjacency_matrix)

    clusters = []
    for cluter_index in range(nb_clusters):
        cluster = np.where(sc.labels_ == cluter_index)[0]
        clusters.append(cluster)

    # compute the normalized cut of the clustering
    normalized_cut = 0
    for cluster in clusters:
        # points that are not in this cluster
        complementary = [x for x in dataset if x not in cluster]
        # print("--")
        # print(cluster)
        # print(complementary)

        # compute the cut of the cluster
        # connections with points outside itsself
        cluster_cut = 0
        for point in cluster:
            point_outside_connections = sum(
                adjacency_matrix[point, complementary])
            cluster_cut += point_outside_connections
        # print(cluster_cut)

        # compute the degree of the cluster
        # it is the sum of the degree of all its nodes
        cluster_degree = 0
        for point in cluster:
            point_degree = sum(adjacency_matrix[point, :])
            cluster_degree += point_degree
        # print(cluster_degree)

        # compute the normalized cut
        cluster_normalized_cut = cluster_cut/cluster_degree
        normalized_cut += cluster_normalized_cut

    print("normalized cut: {}".format(normalized_cut))
    return normalized_cut


normalized_cuts = []
max_nb_clusters = 10
tried_nb_clusters = range(1, max_nb_clusters)
