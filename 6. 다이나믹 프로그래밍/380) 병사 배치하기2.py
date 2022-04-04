n=int(input())
array=list(map(int,input().split()))

d=[1]*n
array.reverse()

for i in range(n):
    for j in range(i):
        if array[i]>array[j]:
            d[i]=max(d[i],d[j]+1)
print(d)
print(n-max(d))

# 7
# 15 11 4 8 5 2 4