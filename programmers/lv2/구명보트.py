def solution(people, limit):
    people.sort()
    answer=0
    a=0
    b=len(people)-1 #마지막 사람
    while a<b:
        if people[a]+people[b]<=limit:
            a+=1
            answer+=1
        b-=1    #가장 작은 a와 같이 못타면 b 혼자타도록 구현
    return len(people)- answer
