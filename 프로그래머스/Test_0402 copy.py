def solution(grid):
    from collections import deque
    alpha=['a','b','c']

    answer=[]
    new_grid=[]
    len_string=''
    for g in grid:
        new_grid.append(list(g))
        len_string+=g
    len_check=min(len(set(len_string)),3)

    count=0
    for i in grid:
        count+=i.count('?')
        
    def change(new_grid,count):
        if count==0:
            array=[[0]*len(new_grid[0]) for _ in range(len(new_grid))]
            tmp=0
            for i in range(len(new_grid)):
                for j in range(len(new_grid[i])):
                    if array[i][j]==0:
                        tmp+=1
                        array=check(i,j,array,new_grid,tmp)
            
            if tmp<=len_check:
                answer.append(1)
            return      
  
        for i in range(len(new_grid)):
            for j in range(len(new_grid[i])):
                if new_grid[i][j]=='?':
                    for x in alpha:
                        new_grid[i][j]=x
                        change(new_grid,count-1)
                    new_grid[i][j]='?'
                    return
        
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]   

    def check(x,y,array,new_grid,tmp):
        q=deque([(x,y)])
        array[x][y]=tmp

        while q:
            x,y=q.popleft()

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if nx<0 or nx>=len(new_grid) or ny<0 or ny>=len(new_grid[0]) or array[nx][ny]>0:
                    continue

                if new_grid[x][y]==new_grid[nx][ny]:
                    array[nx][ny]=array[x][y]
                    q.append((nx,ny))
        return array

    change(new_grid,count)

    return sum(answer)

print(solution(["???", "abc", "cc?"]))
print(solution(["aa?"]))