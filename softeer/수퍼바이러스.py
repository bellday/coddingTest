***
문제
수퍼바이러스가 숙주의 몸속에서 0.1초당 P배씩 증가한다.
처음에 수퍼바이러스 K마리가 있었다면 N초 후에는 총 몇 마리의 수퍼바이러스로 불어날까?
N초 동안 죽는 수퍼바이러스는 없다고 가정한다.
수퍼바이러스는 일반 바이러스에 비해서 훨씬 오래 생존할 수 있기 때문에 N이 매우 클 수 있다.

제약조건
1 ≤ K ≤ 108 인 정수
1 ≤ P ≤ 108 인 정수
1 ≤ N ≤ 1016 인 정수


***
k,p,n = map(int,input().split())
p=p**(10)
def virus(p,n):

    if n ==1:
        return p
    elif n%2 ==0:
        num = virus(p,n/2)
        return num*num %1000000007
    elif n%2==1:
        num2 = virus(p,(n-1)/2)
        return num2 * num2 *p %1000000007
k=k*virus(p,n)
print(k%1000000007)
