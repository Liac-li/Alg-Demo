# Single source shortest path

import numpy as np
import sys
import queue
from typing import Tuple

from myutils import genUndirectedAdjMatrix, getMatrixFromFile
from color_util import set_color, COLOR
from basic import TopologicalSort


def PushDagSSSP(graph: np.ndarray, src: int) -> Tuple[list, list]:
    """
        Based on Topological Order of DAG
    """
    V = graph.shape[0]
    assert 0 <= src < V, 'src out of range, not in graph'

    MAX = sys.maxsize

    # Initialize SSSP 
    dist = [MAX] * V
    dist[src] = 0
    pred = [None] * V
    topoOrder = TopologicalSort(graph) # ! Topological order is not unique

    # Relex tense edge
    start = topoOrder.index(src)
    for u in topoOrder[start:]:
        for v in np.nonzero(graph[u])[0]:
            if dist[u] == MAX:
                # Some nodes may not reachable with each other may lead to 
                # various topological order, which leads to wrong accessing order
                continue  
            if dist[v] > dist[u] + graph[u, v]:
                dist[v] = dist[u] + graph[u, v]
                pred[v] = u
    dist = [i if i != MAX else None for i in dist]
    return dist, pred


def SSSP_BFS(graph: np.ndarray, src: int) -> Tuple[list, list]:
    """
        Only with dist as 1
    """
    V = graph.shape[0]
    assert 0 <= src < V, 'src out of range, not in graph'
    MAX = sys.maxsize

    # init
    dist = [0] + [MAX] * (V - 1)
    prev = [None] * V

    que = queue.Queue()
    que.put(src)
    while not que.empty():
        cur = que.get()
        for v in np.nonzero(graph[cur])[0]:
            if dist[v] > dist[cur] + 1:
                dist[v] = dist[cur] + 1
                prev[v] = cur
                que.put(v)
    return dist, prev


if __name__ == '__main__':

    xs, infors = getMatrixFromFile([3])
    dist, pred = PushDagSSSP(xs[0], 4)
    print(dist, pred)
