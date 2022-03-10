from itertools import combinations

# orders로 모든 조합 뽑아내고 개수 세기
def solution(orders, course):
    answer = []
    for num in course:
        tmp={}
        for i in orders:
            for j in list(combinations(sorted(i), num)):
                if "".join(j) in tmp.keys():
                    tmp["".join(j)]+=1
                else:
                    tmp["".join(j)]=1
                    
        if len(tmp)>0:
            max_value=max(tmp.values())
            if max_value>1:
                for k,v in tmp.items():
                        if v==max_value:
                            answer.append(k)

    return sorted(answer)


#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

# 시간 초과 
def solution(orders, course):
    answer = []

    sumlist="".join(orders)
    sumlist=sorted(set(sumlist))

    for num in course:
        tmp={}
        for i in list(combinations(sumlist, num)):
            count=0
            for j in orders:
                if len(list(set(i) & set(j)))==num :
                    count+=1
            if count>1:
                tmp["".join(i)]=count

        if len(tmp)>0:
            max_value=max(tmp.values())
            for k,v in tmp.items():
                if v==max_value:
                    answer.append(k)

    return sorted(answer)


import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]