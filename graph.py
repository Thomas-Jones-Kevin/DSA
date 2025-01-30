#graph

n = 8 #vertices
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]] #edges

#Adajacency matrix

M = []
for i in range(n):
    M.append([0]*n)

for u,v in A:
    M[u][v] = 1

print(M)

#Adajacency list
from collections import defaultdict

al = defaultdict(list)
for u,v in A:
    al[u].append(v)

print(al)

#recursive Dfs
'''
def dfs1(source):
    #print(source)
    for i in al[source]:
        if i not in visited:
            visited.add(i)
            dfs1(i)
    
'''
visited = set()
source = 0
#dfs1(source)

#iterative dfs
print("dfs")
def dfs2(source):
    visited = set()
    stack = [source]
    visited.add(source)
    while stack:
        node = stack.pop()
       # visited.add(node)
        print(node)
        for i in al[node]:
            if i not in visited:
                visited.add(i)
                stack.append(i)    

print(dfs2(0))

#bfs
print("BFS")
from collections import deque
def bfs(source):
    seen = set()
    queue = deque()
    queue.append(source)
    while queue:
        node = queue.popleft()
        print(node)
        for i in al[node]:
            if i not in seen:
                queue.append(i)
                seen.add(i)
bfs(0)






