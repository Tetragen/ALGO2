"""
    build an affinity matric and apply Spectral Clustering
"""

from sklearn.cluster import SpectralClustering
import numpy as np

adjacency_matrix = np.random.randint(0, 2, (10, 10))
adjacency_matrix = np.zeros((14, 14))

# Implement the adjacency matrix
# cluster 1
adjacency_matrix[0, [1, 2]] = 1
adjacency_matrix[1, [0, 3, 2, 5]] = 1
adjacency_matrix[2, [0, 1, 5, 4]] = 1

# cluster 2
adjacency_matrix[6, [1, 9]] = 1

# cluster 3
adjacency_matrix[9, [12, 13]] = 1
adjacency_matrix[13, [9, 11, 12]] = 1

transp = np.transpose(adjacency_matrix)
print(np.where(adjacency_matrix-transp))
print(adjacency_matrix)

nb_datapoints = adjacency_matrix.shape[0]
dataset = [x for x in range(nb_datapoints)]

# CHANGE HERE
# choose a relevant number of clusters
nb_clusters = 2

sc = SpectralClustering(nb_clusters, affinity='precomputed')

# apply the Spectral Clustering to the adjacency matrix
sc.fit_predict(adjacency_matrix)

# print the clusters
for cluster_index in range(nb_clusters):
    cluster = np.where(sc.labels_ == cluster_index)[0]
    print("cluster {}".format(cluster_index))
    print(cluster)
