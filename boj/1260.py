from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
dfs_visit = [False] * (n + 1)
dfs_list = []
bfs = []
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1



def dfs(v):
    dfs_visit[v]=True
    dfs_list.append(v)
    for i in range(n+1):
        if graph[v][i]==1 and dfs_visit[i]== False:
            dfs(i)





queue = deque([v])
visited[v] = True
dfs(v)
while queue:

    loca = queue.popleft()
    bfs.append(loca)

    for i in range(1, n + 1):
        if graph[loca][i] == 1 and visited[i] == False:
            visited[i] = True
            queue.append(i)
for k in dfs_list:
    print(k,end=' ')
print()
for b in bfs:
    print(b,end=' ')

