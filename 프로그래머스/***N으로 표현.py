def solution(N, number):
    dp=[0]*(number+1)

    for i in range(1,number+1):
        dp[i]=dp[i-1]+2
        
        if i>=N:
            if i%N==0:
                dp[i]=min(dp[i],dp[i-N]+1)
            else:
                dp[i]=min(dp[i],dp[i//N*N]+2*(i%N))
    print(dp)
    return dp[number]


print(solution(5,12))