import numpy as np

from myutils import genUndirectedAdjMatrix, getMatrixFromFile
from color_util import set_color, COLOR


def getConnectedComponent(graph:np.ndarray) -> int:
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
            unvisited_node.remove(cur_node)
            for neighbor in np.nonzero(graph[cur_node])[0]:
                if neighbor in unvisited_node:
                    stack.append(neighbor)
    return cnt_component

def JarnikMST(graph:np.ndarray) -> np.ndarray:
    """
    Jarnik's algorithm
    """
    # get connected component
    cnt_component = getConnectedComponent(graph)
    # get the minimum spanning tree
    mst = np.zeros_like(graph)
    for i in range(cnt_component):
        # get the minimum spanning tree of each component
        mst_i = np.zeros_like(graph)
        for j in range(graph.shape[0]):
            if j == i:
                continue
            # get the minimum spanning tree of each component
            mst_i[j] = graph[j] - graph[i]
        # get the minimum spanning tree of each component
        mst_i = mst_i.argmin(axis=1)
        # get the minimum spanning tree of each component
        mst[i] = mst_i
    return mst

if __name__ == "__main__":

    xs, infos = getMatrixFromFile([1])
    print(set_color(f"Number of Component: {getConnectedComponent(xs[0])}", COLOR.BLUE), infos[0])