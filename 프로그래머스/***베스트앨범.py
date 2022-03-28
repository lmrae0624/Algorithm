def solution(genres, plays):
    answer = []
   
    graph={i:[] for i in set(genres)}
    total={i:0 for i in genres}

    for i in range(len(genres)):
        graph[genres[i]].append([plays[i],i])
        total[genres[i]]+=plays[i]

    for key in sorted(total, key=lambda x : total[x], reverse=True):
        tmp=graph[key]
        tmp.sort(key= lambda x: (-x[0],x[1]))

        for i in range(2):
            if tmp:
                answer.append(tmp.pop(0)[1])
    
    return answer

print(solution(["classic", "pop", "classic", "classic"],[500, 150, 500, 2500]))