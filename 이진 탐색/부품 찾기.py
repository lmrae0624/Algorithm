# 이진 탐색 방법
n=int(input())
array=list(map(int,input().split()))
m=int(input())
find_array=list(map(int,input().split()))

array.sort()

for find in find_array:
    start=0
    end=n-1
    result=-1
    while start<=end:
        mid=(start+end)//2

        if array[mid]==find:
            result=mid
            break
        elif array[mid] > find:
            end=mid-1
        else:
            start=mid+1
    print('no' if result==-1 else 'yes' ,end=' ')

# 입력 
# 5
# 8 3 7 9 2
# 3
# 5 7 9


# 계수 정렬 방법
d=[0]*1000001

for a in array:
    d[a]=1
# 이렇게 반복문도 가능
# for i in input().split():
#     array[int(i)] = 1

for find in find:
    if d[find]==1:
        print('yes',end=' ')
    else:
        print('no',end=' ')


# 집합(Set) 자료형 방법
for find in find_array:
    if find in array:
        print('yes', end=' ')
    else: 
        print('no', end=' ')
