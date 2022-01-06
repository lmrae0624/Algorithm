n=int(input())
array=list(map(int,input().split()))

def binary(array,start,end):
    while start<=end:
        mid=(start+end)//2

        if array[mid]==mid:
            return mid
        elif array[mid]>mid:
            end=mid-1
        else:
            start=mid+1
    return -1

print(binary(array,0,n-1))

# 입력
# 5
# -15 -6 1 3 7

# 7
# -15 -4 2 8 9 13 15

# 7
# -15 -4 3 8 9 13 15