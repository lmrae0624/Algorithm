n=int(input())
graph=[]
teacher_location=[]

total_student=0
for i in range(n):
    tmp=list(map(str,input().split()))
    graph.append(tmp)

    for j in range(n):
        if tmp[j]=='T':
            teacher_location.append((i,j))
        elif tmp[j]=='S':
            total_student+=1


def student_count(tmp):
    count=0
    for i in range(n):
        for j in range(n):
            if tmp[i][j]=='S':
                count+=1  
    return count


def teacher_view(tmp):
    for i in teacher_location:
        x=i[0]
        y=i[1]

        for i in range(n):
            ny=y-i
            if 0>ny or tmp[x][ny]=='O':
                break
            tmp[x][ny]='T'

        for i in range(n):
            ny=y+i
            if ny>=n or tmp[x][ny]=='O':
                break
            tmp[x][ny]='T'

        for i in range(n):
            nx=x-i
            if 0>nx or tmp[nx][y]=='O':
                break
            tmp[nx][y]='T'

        for i in range(n):
            nx=x+i
            if nx>=n or tmp[nx][y]=='O':
                break
            tmp[nx][y]='T'
    return tmp

    
result=0
tmp=[[0]*n for _ in range(n)]

def solution(wall):
    global result,tmp    
    if wall==3:
        for i in range(n):
            for j in range(n):
                tmp[i][j]=graph[i][j]
       
        tmp=teacher_view(tmp)
        result=max(result,student_count(tmp))
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j]=='X':
                graph[i][j]='O'
                wall+=1
                solution(wall)
                wall-=1
                graph[i][j]='X'
    
solution(0)
if result==total_student:
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