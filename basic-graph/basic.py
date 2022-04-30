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


if __name__ == "__main__":

    xs, infos = getMatrixFromFile([1])
    print(set_color(f"Number of Component: {getConnectedComponent(xs[0])}", COLOR.BLUE), infos[0])