def solution(n, clockwise):
    answer = [[0]*n for _ in range(n)]
    
    tmp=1
    answer[0][0]=tmp
    answer[0][n-1]=tmp 
    answer[n-1][0]=tmp
    answer[n-1][n-1]=tmp

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]



    

    return answer

#print(solution(5,True))


