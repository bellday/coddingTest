n=int(input())
house=[]
graph=[]
cnt=0
h=0

def dfs(x,y):
    global  h
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y] =0
        h+=1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True


    return False

for _ in range(n):
    graph.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            cnt+=1
            house.append(h)
            h=0

house.sort()

print(cnt)

for h in house:
    print(h)


