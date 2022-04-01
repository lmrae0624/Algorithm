n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(array[i])):
        left,right=0,0
        
        if j>0:
            left=array[i-1][j-1]

        if j<len(array[i])-1: #i!=j
            right=array[i-1][j]
        array[i][j]=max(left,right)+array[i][j]

print(max(array[n-1]))

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5