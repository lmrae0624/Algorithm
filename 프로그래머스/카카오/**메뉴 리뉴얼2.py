def solution(orders, course):
    from itertools import combinations
    answer = []
    
    for c in course:
        new={}
        for order in orders:
            for com in combinations(sorted(order),c):
                key="".join(com)
                new[key]=new.get(key,0)+1
        
        if len(new)>1:
            max_value=max(new.values())
            if max_value>1:
                for key,value in new.items():
                    if value==max_value:
                        answer.append(key)

    answer.sort()
    
    return answer


#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

