n=int(input())
stages=list(map(int,input().split()))

sum=len(stages)
array=[]
for i in range(1,n+1):
    stagecount=stages.count(i)
    array.append((i, stagecount/sum))
    sum-=stagecount

array=sorted(array,key=lambda x:-x[1])
for i in array:
    print(i[0],end=' ')

# 5
# 2 1 2 6 2 4 3 3

# 4
# 4 4 4 4 4