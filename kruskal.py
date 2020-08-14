import numpy as np
from disjoint_set import DisjointSet


def kruskal(points):
    """finds minimum spanning tree of given points

    :param points: numpy array of shape (n_points, 2)
    :return: array of tuples (length, vertex_1, vertex_2) - edges of minimum spanning tree
    """
    length = points.shape[0]
    disjoint_set = DisjointSet(length)
    edges = [(np.linalg.norm(points[i] - points[j]), i, j)
             for i in range(length) for j in range(i + 1, length)]
    edges.sort(key=lambda x: x[0])
    adjacency_list = [[] for _ in range(length)]
    for w, u, v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            disjoint_set.union(u, v)
    return adjacency_list
