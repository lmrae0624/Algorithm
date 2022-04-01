n=int(input())

graph=[]
teacher=[]
student=0
for i in range(n):
    graph.append(list(map(str,input().split())))

    for j in range(n):
        if graph[i][j]=='T':
            teacher.append((i,j))
        elif graph[i][j]=='S':
            student+=1

tmp=[['X']*n for _ in range(n)]

def teacher_view(tmp):
    global teacher
    
    for t in teacher:
        x=t[0]
        y=t[1]

        for i in range(1,n):
            nx=x+i
            if nx>=n or tmp[nx][y]=='O':
                break
            tmp[nx][y]='T'

        for i in range(1,n):
            nx=x-i
            if nx<0 or tmp[nx][y]=='O':
                break
            tmp[nx][y]='T'

        for i in range(1,n):
            ny=y+i
            if ny>=n or tmp[x][ny]=='O':
                break
            tmp[x][ny]='T'

        for i in range(1,n):
            ny=y-i
            if ny<0 or tmp[x][ny]=='O':
                break
            tmp[x][ny]='T'
    
    return count(tmp)

def count(tmp):
    cnt=0
    for i in range(n):
        for j in range(n):
            if tmp[i][j]=='S':
                cnt+=1
    return cnt

result=0
def wall_creat(wall,graph):
    global result
    if wall==3:
        for i in range(n):
            for j in range(n):
                tmp[i][j]=graph[i][j]
        
        result=max(result,teacher_view(tmp))
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j]=='X':
                graph[i][j]='O'
                wall_creat(wall+1,graph)
                graph[i][j]='X'

wall_creat(0,graph)
if result==student:
    print('YES')
else:
    print('NO')

# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# 4
# S S S T
# X X X X
# X X X X
# T T T X