def binary(array,target,start,end):
    if start>end:
        return -1
    
    mid=(start+end)//2

    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return binary(array,target,start,mid-1)
    else:
        return binary(array,target,mid+1,end)

n,target=map(int,input().split())
array=list(map(int,input().split()))

result=binary(array,target,0,n-1)
print(result)


# 입력 예시
# 10 7
# 1 3 5 7 9 11 15 17 19
