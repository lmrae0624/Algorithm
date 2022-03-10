def solution(clothes):
    answer = 1
    type=[t for i,t in clothes]
    type=list(set(type))

    item=[0]*len(type)
    
    for i,t in clothes:
        item[type.index(t)]+=1

    for i in item:  
        answer*=(i+1)
    
    return answer-1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))


def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
