lottos=list(map(int,input().split(',')))
win_nums=list(map(int,input().split(',')))
answer=[]

right=0
for i in win_nums:
    if i in lottos:
        right+=1

max_result=7-(right+lottos.count(0))
min_result=7-right

answer.append(6 if max_result==7 else max_result)
answer.append(6 if min_result==7 else min_result)

print(answer)

def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]