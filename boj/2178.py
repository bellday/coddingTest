# n,m 입력으로 받는다
# 지문상 n,m 배열에선 n-1, m-1 을 만나면 break 건다
# bds 가 필요함, queue 사용요망
# 시간복잡도 100* 100 * 5

from collections import deque

# 입력

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 이동 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 1
queue = deque([(0, 0, cnt)])

while queue:
    x, y, d = queue.popleft()

    if x == n - 1 and y == m - 1:
        print(d)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny, d + 1))
