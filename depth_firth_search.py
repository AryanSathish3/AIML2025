from collections import deque
graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}
def dfs_using_stact(graph,start):
    stack=[start]
    visited=set()
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex])
dfs_using_stact(graph,'A')
