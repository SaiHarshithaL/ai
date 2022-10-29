from sys import maxsize
from itertools import permutations
v=4
def travelsp(graph,s):
    vertex=[]
    for i in range(v):
        if(i!=s):
            vertex.append(i)
    minpath=maxsize
    np=permutations(vertex)
    for i in np:
        cp=0
        k=s
        for j in i:
            cp+=graph[k][j]
            k=j
        cp+=graph[k][s]
        minpath=min(minpath,cp)
    return minpath
graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
s=0
print(travelsp(graph,s))

    