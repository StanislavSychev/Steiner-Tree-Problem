import numpy as np
import matplotlib.pyplot as plt
from fermat_point import fermat_point
from kruskal import kruskal
from utils import visualize_tree


def add_steiner_points(points, adjacency_list):
    """add Steiner points"""
    terminal_size = points.shape[0]
    new_point = terminal_size
    for y, incident_y in enumerate(adjacency_list):
        # need to check only terminal - terminal edges
        if y >= terminal_size:
            break
        for x in incident_y:
            # need to check only terminal - terminal edges
            if x >= terminal_size:
                break
            # find adjacent edge with minimum angle
            min_angle = np.pi
            min_z = None
            for z in incident_y:
                # can't check new steiner points edges
                if np.linalg.norm(points[y] - points[z]) == 0.0:
                    continue
                # no need to check angle with self
                if x == z:
                    continue
                vx = points[x] - points[y]
                vz = points[z] - points[y]
                angle = np.arccos(np.clip(np.dot(vx, vz) / (np.linalg.norm(vx) * np.linalg.norm(vz)), -1, 1))
                # make absolute angle
                if angle > np.pi:
                    angle = 2 * np.pi - angle
                if angle < min_angle:
                    min_angle = angle
                    min_z = z
            # if angle less than 120, Steiner point between 3 vertexes can help
            if min_angle < 120 * np.pi / 180:
                incident_y.remove(x)
                incident_y.remove(min_z)
                incident_y.append(new_point)
                adjacency_list[x].remove(y)
                adjacency_list[x].append(new_point)
                adjacency_list[min_z].remove(y)
                adjacency_list[min_z].append(new_point)
                incident_new = [x, y, min_z]
                incident_new.sort()
                adjacency_list.append(incident_new)
                new_point += 1
                points = np.vstack((points, points[y]))
    return points, adjacency_list


def move_steiner_points(points, adjacency_list, terminal_size, iterations=1000, alpha=0.01):
    """moves Steiner points to proper places, by moving towards its neighbours Fermat point"""
    for _ in range(iterations):
        for e in range(terminal_size, points.shape[0]):
            points[e] += alpha * (fermat_point(
                points[adjacency_list[e][0]],
                points[adjacency_list[e][1]],
                points[adjacency_list[e][2]]
            ) - points[e])
    return points, adjacency_list


def heuristic_tree(points, iterations=1000, alpha=0.01):
    """heuristic algorithm for Steiner tree."""
    size = points.shape[0]
    adjacentcy_list = kruskal(points)
    points, adjacentcy_list = add_steiner_points(points, adjacentcy_list)
    points, adjacentcy_list = move_steiner_points(points, adjacentcy_list, size, iterations=iterations, alpha=alpha)
    return points, adjacentcy_list


if __name__ == '__main__':
    np.random.seed(42)
    size = 5
    p = np.random.uniform(0, 1, (size, 2))
    p, al = heuristic_tree(p)
    visualize_tree(p, al, size)
