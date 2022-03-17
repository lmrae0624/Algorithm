def solution(n):
    answer = [[0]*n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    tmp=1
    index=0
    x,y=0,0
    answer[x][y]=tmp
    while tmp<n*n:
        nx=x+dx[index]
        ny=y+dy[index]

        if 0>nx or nx>=n or 0>ny or ny>=n:
            index=(index+1) % 4
            continue

        if answer[nx][ny]==0:
            tmp+=1
            answer[nx][ny]=tmp
            x,y=nx,ny
        else:
            index=(index+1) % 4

    return answer

print(solution(6))
