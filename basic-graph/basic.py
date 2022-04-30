from inspect import currentframe
import numpy as np
from queue import PriorityQueue

from myutils import genUndirectedAdjMatrix, getMatrixFromFile
from color_util import set_color, COLOR


def getConnectedComponent(graph:np.ndarray) -> int:
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

def JarnikMST(graph:np.ndarray) -> np.ndarray:
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
    while len(unvisited_node) > 0:
        # print(cur_node, unvisited_node)

        neighbors = np.nonzero(graph[cur_node])[0]
        for neighbor in neighbors:
            if neighbor in unvisited_node:
                component_edges.put((graph[cur_node, neighbor], (cur_node, neighbor)))
        unvisited_node.remove(cur_node)

        min_safe_edge = component_edges.get()
        while all(node not in unvisited_node for node in min_safe_edge[1]) and not component_edges.empty():
            min_safe_edge = component_edges.get()

        x, y = min_safe_edge[1]
        mst[x, y] = min_safe_edge[0]
        mst[y, x] = min_safe_edge[0]
        cur_node = y
    
    return mst

    
    
if __name__ == "__main__":

    xs, infos = getMatrixFromFile([1])
    print(set_color(f"Number of Component: {getConnectedComponent(xs[0])}", COLOR.BLUE), infos[0])
    
    xs, infos = getMatrixFromFile([2]) 
    assert getConnectedComponent(xs[0]) >= 1
    mst = JarnikMST(xs[0])
    assert getConnectedComponent(mst) == 1
    print(set_color(f"mst: \n{mst}", COLOR.BLUE), infos[0])