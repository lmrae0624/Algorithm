n,target=map(int,input().split())
array=list(map(int,input().split()))

start=0
end=n-1
result=-1
# while True:
#     if start>end:
#         break

while start <= end:
    mid=(start+end)//2

    if array[mid] == target:
        result=mid+1
        break
    elif array[mid] > target:
        end=mid-1
    else:
        start=mid+1

print(result)