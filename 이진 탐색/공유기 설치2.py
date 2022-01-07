n, c=map(int,input().split())
array=[int(input()) for _ in range(n)]
array.sort()

start=1
end=array[-1]
result=0
while start <= end:
    value=array[0]
    count=1
    mid=(start+end)//2
    
    for i in range(1,n):
        if array[i] >= value+mid:
            count+=1
            value=array[i]
    
    if count>=c:
        result=mid
        start=mid+1
    else:
        end=mid-1
print(result)
