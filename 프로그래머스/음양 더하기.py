from xmlrpc.client import Boolean


absolutes=list(map(int,input().split(',')))
signs=list(map(str,input().split(',')))

answer=0
for i in range(len(absolutes)):
    if signs[i]=='false':
        answer-=absolutes[i]
        continue
    answer+=absolutes[i]
print(answer)


# 4,7,12
# true,false,true

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
