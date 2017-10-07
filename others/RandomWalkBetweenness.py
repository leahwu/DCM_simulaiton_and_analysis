import random
import networkx as nx
from networkx.algorithms.centrality.flow_matrix import *

def random_walk_betweenness_centrality(G, normalized=True, weight='weight', dtype=float, solver='full'):
    try:
        import numpy as np
    except ImportError:
        raise ImportError('current_flow_betweenness_centrality requires NumPy ',
                          'http://scipy.org/')
    try:
        import scipy
    except ImportError:
        raise ImportError('current_flow_betweenness_centrality requires SciPy ',
                          'http://scipy.org/')

    n = G.number_of_nodes()
    H = G.copy()

    betweenness = dict.fromkeys(H, 0.0)  # b[v]=0 for v in H
    for row, (s, t) in flow_matrix_row(H, weight=weight, dtype=dtype,
                                       solver=solver):
        pos = dict(zip(row.argsort()[::-1], range(n)))
        for i in range(n):
            betweenness[s] += (i - pos[i]) * row[i]
            betweenness[t] += (n - i - 1 - pos[i]) * row[i]
    if normalized:
        nb = (n - 1.0) * (n - 2.0)  # normalization factor
    else:
        nb = 2.0
    for v in H:
        betweenness[v] = float((betweenness[v] - v) * 2.0 / nb)
    return dict((ordering[k], v) for k, v in betweenness.items())

