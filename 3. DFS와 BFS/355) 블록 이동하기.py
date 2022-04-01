from collections import deque
def next_positon(pos,new_board):
    pos=list(pos)
    x1,y1=pos[0][0],pos[0][1]
    x2,y2=pos[1][0],pos[1][1]

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    next_list=[]
    for i in range(4):
        nx1,ny1=x1+dx[i], y1+dy[i]
        nx2,ny2=x2+dx[i], y2+dy[i]

        if new_board[nx1][ny1]==0 and new_board[nx2][ny2]==0:
            next_list.append({(nx1,ny1),(nx2,ny2)})
    
    if x1==x2: #가로
        for i in [-1,1]:
            if new_board[x1+i][y1]==0 and new_board[x2+i][y2]==0:
                next_list.append({(x1,y1),(x1+i,y1)})
                next_list.append({(x2,y2),(x2+i,y2)})
    elif y1==y2: #세로
        for i in [-1,1]:
            if new_board[x1][y1+i]==0 and new_board[x2][y2+i]==0:
                next_list.append({(x1,y1),(x1,y1+i)})
                next_list.append({(x2,y2),(x2,y2+i)})
    
    return next_list

def solution(board):
    n=len(board)

    new_board=[[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1]=board[i][j]
    
    q=deque()
    visited=[]
    now={(1,1),(1,2)} 
    q.append((now,0))
    visited.append(now)

    while q:
        pos,cost=q.popleft()

        if (n,n) in pos:
            return cost
        
        for next in next_positon(pos,new_board):
            if next not in visited:
                visited.append(next)
                q.append((next,cost+1))

    return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))