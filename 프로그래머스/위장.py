from itertools import product
def solution(clothes):
    answer = 0

    type=[]
    for c in clothes:
        type.append(c[1])
 
    dict={key:[] for key in set(type)} 

    for c in clothes:
        dict[c[1]].append(c[0])


    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))