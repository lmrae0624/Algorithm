
def solution(n, words):
    answer = [0,0]

    pre=words[0][-1]   
    i=1
    count=1
    tmp=[words[0]]
    for w in words[1:]:
        i+=1

        if (i-1)%n==0:
            count+=1
            i=1

        if pre!=w[0] or w in tmp:
            answer=[i,count]
            break

        pre=w[-1]
        tmp.append(w)
        
    return answer

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))


def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]