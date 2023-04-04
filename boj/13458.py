clas = int(input())
#clas = 1000000
a=list(map(int,input().split(' ')))
#a=[1000000 for i in range(1000000)]
teacher=list(map(int,input().split(' ')))
cnt=0
for i in a:
    i=i-teacher[0]#main 감독관 1명 
    cnt+=1
    if i%teacher[1]==0:# sub 감독관 계산
        cnt+=i//teacher[1]
    else:
        cnt+=(i//teacher[1])+1
print(cnt)