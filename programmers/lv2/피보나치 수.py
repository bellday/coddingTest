def solution(n):
    
    fivo=[0,1]
    
    for i in range(2,n+1):
        fivo.append(fivo[len(fivo)-1]+fivo[len(fivo)-2])
    return fivo[len(fivo)-1]%1234567
