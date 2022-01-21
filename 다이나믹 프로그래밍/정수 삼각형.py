n=int(input())
array=[]
for _ in range(n):
    array.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(array[i])):
        tmp=0

        if j<len(array[i-1]):
            tmp=max(tmp,array[i][j]+array[i-1][j])
        if j>=1:
            tmp=max(tmp,array[i][j]+array[i-1][j-1])

        array[i][j]=tmp
        
print(max(array[n-1]))