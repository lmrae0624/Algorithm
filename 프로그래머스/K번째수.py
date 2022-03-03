array=list(map(int,input().split(',')))
commands=[list(map(int,input().split(','))) for i in range(3)]

answer = []
for com in commands:
    a,b,r=com
    tmp=array[a-1:b]
    tmp.sort()
    answer.append(tmp[r-1])

print(answer)

# 1, 5, 2, 6, 3, 7, 4
# 2,5,3
# 4,4,1
# 1,7,3

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))