
def solution(grid, k):
    from collections import deque
    answer = 0
    n, m = len(grid), len(grid[0])
    move_count=[[0]*len(grid[0]) for _ in range(len(grid))] 

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
 
    q=deque([(0, 0, 0, 0)])
    while q:
        move, camp, x, y= q.popleft()
        print(move_count)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m or grid[nx][ny]=='#':
                continue
           
            if move_count[nx][ny]==0: #처음 방문하는 경우
                move_count[nx][ny]=move+1
                
                if move+1 > k :
                    answer+=1
                    move=0
                    
                q.append((move+1,answer,nx,ny))

    return answer

print(solution(["..FF", "###F", "###."],4))
print(solution(["..FF", "###F", "###."],5))



    # def dfs(move_count,x,y):
    #     for i in range(4):
    #         nx=x+dx[i]
    #         ny=y+dy[i]

    #         if nx<0 or nx>=n or ny<0 or ny>=m :
    #             continue

    #         if grid[nx][ny]=='.' or grid[nx][ny]=='F':
    #             move_count[nx][ny]=move_count[x][y]+1
    #             if move_count==k:
    #                 camp_count[nx][ny]+=1