n,m = map(int, input().split())
r,c,d=map(int, input().split())
graph= [list(map(int,input().split())) for _ in range(n)]

# 0: 북 1: 동 2: 남 3: 서
dx=[-1,0,1,0]#세로
dy=[0,1,0,-1]#가로
cnt=0

while 1:

    #청소
    if graph[r][c]==0:
        graph[r][c]=2
        cnt +=1

    for i in range(4):
        d = (d + 3) % 4
        nr= r+ dx[d]
        nc= c+ dy[d]
        if 0<= nr < n and 0<= nc < m:
            if graph[nr][nc]==0:
                r =nr
                c= nc

                break

    else: #청소된
        nr= r-dx[d]
        nc = c - dy[d]
    if 0 <= nr < n and 0 <= nc < m:
        if graph[nr][nc]==1:
            break
        else:
            r= nr
            c =nc

print(cnt)
