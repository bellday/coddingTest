from collections import deque
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]


while True:
    y,x=map(int,input().split())#가로 세로
    if x==0 and y==0:
        break
    graph=[list(map(int,input().split())) for _ in range(x)]
    visited=[[False]*y for _ in range(x)]
    cnt=0
    for i in range(x):
        for j in range(y):
            if graph[i][j]==1 and visited[i][j]==False:
    
                cnt+=1
                queue=deque([(i,j)])
                visited[i][j]=True
                while queue:
                    a,b=queue.popleft()
                    
                    for k in range(8):
                        ni = a+dx[k]
                        nj= b+dy[k]
                        if 0<=ni<x and 0<=nj < y and graph[ni][nj]==1 and  not visited[ni][nj]:
                            
                            visited[ni][nj]=True
                            queue.append((ni,nj))
    #print()                        
    print(cnt)
