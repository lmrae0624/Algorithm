from cmath import cos


def solution(money, costs):
    answer = 0
    m=[1,5,10,50,100,500]

    d=[0]*len(costs)
    d[0]=costs[0]
    d[1]=min(costs[1],d[0]*5)

    for i in range(2,len(costs)):
        if i%2==0: #5 50 500원
            d[i]=min(costs[i],d[i-1]*2,d[i-2]*10)
        else: #1 10 100원
            d[i]=min(costs[i],d[i-1]*5,d[i-2]*10)

    for i in range(len(m)-1,0,-1):
        answer+=(money//m[i])*d[i]
        money=money%m[i]

    return answer+money*d[0]


print(solution(4578,[1, 4, 99, 35, 50, 1000]))
print(solution(1999,[2, 11, 20, 100, 200, 600]))