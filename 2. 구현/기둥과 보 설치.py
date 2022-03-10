n=int(input())
array=[]
while True:
    tmp=input()
    if tmp=='':
        break
    array.append(list(map(int,tmp.split())))

def check(graph):
    for alist in graph:
        x,y,a=alist
        if a==0:
            if y==0 or [x,y-1,0] in graph or [x,y,1] in graph or [x-1,y,1] in graph:
                continue
        elif a==1:
            if [x,y-1,0] in graph or [x+1,y-1,0] in graph or ([x-1,y,1] in graph and [x+1,y,1] in graph):
                continue
        return False
    return True


graph=[]
while array:
    x,y,a,b=array.pop(0)

    if b==0:
        graph.remove([x,y,a])
        if not check(graph):
            graph.append([x,y,a])
    if b==1:
        graph.append([x,y,a])
        if not check(graph):
            graph.remove([x,y,a])
print(sorted(graph))


# 5
# 1 0 0 1
# 1 1 1 1
# 2 1 0 1
# 2 2 1 1
# 5 0 0 1
# 5 1 0 1
# 4 2 1 1 
# 3 2 1 1
#출력 [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

# 5
# 0 0 0 1
# 2 0 0 1
# 4 0 0 1
# 0 1 1 1
# 1 1 1 1
# 2 1 1 1
# 3 1 1 1
# 2 0 0 0
# 1 1 1 0
# 2 2 0 1
#[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]