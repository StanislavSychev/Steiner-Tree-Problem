import numpy as np
import matplotlib.pyplot as plt


def read_points(path):
    with open(path, 'r') as f:
        points = f.readlines()
        points = [p.strip('\n').split() for p in points]
        points = np.array(points).astype('float')
        return points


def write_tree(path, points, adjacentcy_list):
    lines = [f"{point[0]} {point[1]} {' '.join([str(v) for v in adjacent])}" for point, adjacent in zip(points, adjacentcy_list)]
    with open(path, 'w') as f:
        f.write('\n'.join(lines))


def visualize_tree(points, adjacency_list, terminal_size):
    edges_list = []
    for u, incident_u in enumerate(adjacency_list):
        for v in incident_u:
            if v > u:
                edges_list.append((np.linalg.norm(points[u] - points[v]), u, v))
    c = np.array([0 if i < terminal_size else 1 for i in range(points.shape[0])])
    steiner_dist = 0.0
    for w, u, v in edges_list:
        steiner_dist += w
        plt.plot([points[u, 0], points[v, 0]], [points[u, 1], points[v, 1]], 'r-')
    plt.scatter(points[:, 0], points[:, 1], c=c)
    plt.title(f"Steiner tree for {terminal_size} points with {points.shape[0] - terminal_size} Steiner points\n"
              f"total length l={steiner_dist}")
    plt.axis("off")
    plt.show()
