from inspect import currentframe
import numpy as np
from queue import PriorityQueue

from myutils import genUndirectedAdjMatrix, getMatrixFromFile
from color_util import set_color, COLOR


def getConnectedComponent(graph: np.ndarray) -> int:
    """
    Get the number of connected component in graph
    by DFS with stack
    """
    unvisited_node = set(range(graph.shape[0]))
    cnt_component = 0
    # do multiple dfs
    stack = []
    while len(unvisited_node) > 0:
        cur_node = next(iter(unvisited_node))
        cnt_component += 1
        # one time dfs
        stack.append(cur_node)
        while stack:
            cur_node = stack.pop()
            if cur_node in unvisited_node:
                unvisited_node.remove(cur_node)
            else:
                continue
            for neighbor in np.nonzero(graph[cur_node])[0]:
                if neighbor in unvisited_node:
                    stack.append(neighbor)
    return cnt_component


def JarnikMST(graph: np.ndarray) -> np.ndarray:
    """
    Jarnik's algorithm
    Also known as Prim's algorithm, Implemnet by add safe edge of connect component 
    to mst subgraph
    """
    # print(graph.shape)
    mst = np.zeros_like(graph)
    np.fill_diagonal(mst, 1)

    unvisited_node = set(range(len(graph)))
    component_edges = PriorityQueue()

    cur_node = next(iter(unvisited_node))
    while unvisited_node:
        # print(cur_node, unvisited_node)

        neighbors = np.nonzero(graph[cur_node])[0]
        for neighbor in neighbors:
            if neighbor in unvisited_node:
                component_edges.put((graph[cur_node,
                                           neighbor], (cur_node, neighbor)))
        unvisited_node.remove(cur_node)

        min_safe_edge = component_edges.get()

        while all([node not in unvisited_node for node in min_safe_edge[1]
                   ]) and not component_edges.empty():  # unsafe edge
            min_safe_edge = component_edges.get()

        x, y = min_safe_edge[1]
        mst[x, y] = min_safe_edge[0]
        mst[y, x] = min_safe_edge[0]
        cur_node = y if y in unvisited_node else x

        if len(
                unvisited_node
        ) == 1:  # ! remove node after add safe edge, will add not needed edge
            break

    return mst


def KruskalMST(graph: np.ndarray) -> np.ndarray:

    class UnionFind:
        """
            Simple implemnet of UnionFind, base on disjoint set
        """

        def __init__(self, n):
            self.parent = np.arange(n) # disrect parent of item x 
            self.rank = np.zeros(n) # referenced num of disjoint set

        def find(self, x):
            if self.parent[x] == x:
                return x
            else:
                return self.find(self.parent[x])

        def union(self, x, y):
            xroot = self.find(x)
            yroot = self.find(y)

            # union by rank
            if self.rank[xroot] > self.rank[yroot]:  # union y to x
                self.parent[yroot] = xroot
            elif self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            else:
                self.parent[xroot] = yroot
                self.rank[yroot] += 1

    assert graph.shape[0] == graph.shape[1]

    mst = np.zeros_like(graph)
    np.fill_diagonal(mst, 1)

    vertices_size = graph.shape[0]

    # init edge sorted set
    edges = PriorityQueue()
    tmp = np.triu(graph)
    for u in range(vertices_size):
        for v in np.nonzero(tmp[u])[0]:
            edges.put((tmp[u, v], (u, v)))

    # init parent
    unionList = UnionFind(vertices_size)

    # kruskal main loop
    while not edges.empty():

        min_edge, (u, v) = edges.get()
        if unionList.find(u) != unionList.find(v):
            unionList.union(u, v)
            mst[u, v] = min_edge
            mst[v, u] = min_edge

    return mst


if __name__ == "__main__":

    xs, infos = getMatrixFromFile([1])
    print(
        set_color(f"Number of Component: {getConnectedComponent(xs[0])}",
                  COLOR.BLUE), infos[0])

    xs, infos = getMatrixFromFile([2])
    assert getConnectedComponent(xs[0]) >= 1
    mst = JarnikMST(xs[0])
    assert getConnectedComponent(mst) == 1
    print(set_color(f"Primmst: \n{mst}", COLOR.BLUE), infos[0])

    xs, infos = getMatrixFromFile([2])
    assert getConnectedComponent(xs[0]) >= 1
    mst = KruskalMST(xs[0])
    assert getConnectedComponent(mst) == 1, set_color(f"mst: \n{mst}", COLOR.BLUE)
    print(set_color(f"Kruskalmst: \n{mst}", COLOR.BLUE), infos[0])