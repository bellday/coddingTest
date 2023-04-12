def solution(players, callings):
    answer = []
    dict_play={}
    rank={}
    for index, value in enumerate(players):
        dict_play[index+1]=value
        rank[value]=index
    for c in callings:
        
        #i=players.index(c)
        x=rank[c]
        rank[c]-=1
        rank[players[x-1]]+=1
        
        
        players[x],players[x-1]=players[x-1],players[x]
        
        #print(players)
    return players
