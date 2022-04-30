import numpy as np

FILE_PATH = 'graph.txt'


def genUndirectedAdjMatrix(range, size: tuple) -> np.ndarray:
    """
    Input:
        range: tuple of num range
        size: tuple of matrix size
    Warning:
        diagonal elements may not be 1
    """
    a = np.random.randint(*range, size=size)
    m = np.tril(a) + np.tril(a, -1).T
    return m

def getMatrixFromFile(target_range) -> np.ndarray:
    
    def getInfo(s:str):
        tmp = s.strip().split(':')
        mId = int(tmp[1]) 
        _, info = tmp[2].split('#')
        return mId, info

    global FILE_PATH
    
    lines = open(FILE_PATH).readlines()
    assert len(lines) > 0

    res = []
    read_matrix = False
    tmp = []
    infos = []
    for line in lines:
        if line.startswith(':'):
            mId, info = getInfo(line)
            if mId in target_range:
                read_matrix = True
                infos.append(info)
        elif line[0].isdigit():
            if read_matrix:
                tmp.append([int(i) for i in line.strip().split()])
        else:         
            read_matrix = False
            res.append(np.array(tmp))
            tmp = []

    if len(tmp) > 0:
        res.append(np.array(tmp))

    return res, infos
        
        

