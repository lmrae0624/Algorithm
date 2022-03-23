n, m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int, input())))

move=[(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x, y):
    if 0>x or x>=n or 0>y or y>=m:
        return False

    if graph[x][y]==0:   
        graph[x][y]=1

        for i in move:
            nx=x+i[0]
            ny=y+i[1]

            dfs(nx,ny)
        return True
        # 이렇게도 표현 가능
        # dfs(x - 1, y)
        # dfs(x, y - 1)
        # dfs(x + 1, y)
        # dfs(x, y + 1)

    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)

# 4 5
# 00110
# 00011
# 11111
# 00000

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
