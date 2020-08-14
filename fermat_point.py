import numpy as np

gamma = 10.0
alpha = 0.05


def fermat_point(a, b, c):
    """calculates Fermat point of triangle

    :param a: numpy array of shape (2, ), vertex coordinates
    :param b: numpy array of shape (2, ), vertex coordinates
    :param c: numpy array of shape (2, ), vertex coordinates
    :return: numpy array of shape (2, ) Fermat point coordinates
    """
    la = np.linalg.norm(b - c)
    lb = np.linalg.norm(c - a)
    lc = np.linalg.norm(a - b)
    p = (la + lb + lc) / 2
    s = np.sqrt(p * (p - la) * (p - lb) * (p - lc))
    tc = lambda x, y, z: \
        ((4 * s + (3 ** 0.5) * (x ** 2 + y ** 2 - z ** 2)) * (4 * s + (3 ** 0.5) * (x ** 2 - y ** 2 + z ** 2))) / \
        (8 * s * (12 * s + (3 ** 0.5) * (x ** 2 + y ** 2 + z ** 2)))
    return tc(la, lb, lc) * a + tc(lb, lc, la) * b + tc(lc, la, lb) * c
