# 동적 프로그래밍(dp) 문제: 점점 값을 쌓아가면서 풀어야함
# 현재의 위치에서 가능한 최대 크기의 정사각형의 한 변의 길이를 dp에 저장한다.

def solution(board):
    answer=0
    n=len(board)
    m=len(board[0])
   
    dp=[[0]*m for _ in range(n)]
    dp[0]=board[0]
    for i in range(1,n):
        dp[i][0]=board[i][0]

    for i in range(1,n):
        for j in range(1,m):
            if board[i][j]==1:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    
    for i in range(n):
        tmp=max(dp[i])
        answer=max(answer,tmp)
  
    return answer*answer

print(solution([[0,1,1],[1,1,1],[1,1,1],[0,0,1]]))
