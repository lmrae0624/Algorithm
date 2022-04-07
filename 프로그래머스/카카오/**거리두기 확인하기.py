def solution(places):
    answer = []
    from collections import deque
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    def bfs(x,y,place):
        visited=[[False]*5 for _ in range(5)]
        q=deque([(x,y)])
        visited[x][y]=True
        dist=0
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if nx<0 or nx>=5 or ny<0 or ny>=5 or visited[nx][ny]:
                    continue
                if place[nx][ny]=='P':
                    return False
                if place[nx][ny]=='O': # 한칸 더 확인 하기 위해 q에 append
                    q.append((nx,ny))
                    visited[nx][ny]==True

            dist+=1
            if dist==2:
                return True
        return True
                
    for place in places:
        check=True
        for i in range(5):
            for j in range(5):
                if not check:
                    break
                
                if place[i][j]=='P':
                    if not bfs(i,j,place):
                        check=False
                      
        if check:
            answer.append(1)
        else:
            answer.append(0)
   
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
                        
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer