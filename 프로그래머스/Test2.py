

def func(i,j,answer,index,n):
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]

    nx=i+dx[index]
    ny=j+dy[index]
    if 0>nx or nx>=n or 0>ny or ny>=n:
        if answer[nx][ny]==0:
            answer[nx][ny]=answer[i][j]+1
        else:
            return False

    return True
                 

def solution(n, clockwise):
    answer = [[0]*n for _ in range(n)]
    
    answer[0][0]=1
    answer[0][n-1]=1
    answer[n-1][0]=1
    answer[n-1][n-1]=1

    index=0
    tmp=1
    while True:
        for i in range(n):
            for j in range(n):
                if answer[i][j]==tmp:
                    check=func(i,j,answer,index,n)
                    index+=1
                    index%=4
        tmp+=1
        if not check:
            index+=1
            index%=4
        
        print(answer)
        if 0==(answer[i].count(0) for i in range(n)) :
            break

    return answer

print(solution(5,True))