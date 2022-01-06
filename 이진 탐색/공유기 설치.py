# 거리를 기준으로 하기
n, c=map(int,input().split())
array=[int(input()) for _ in range(n)]
array.sort()

start=1
end=array[-1]-array[0]
result=0

while start<=end:
    count=1 # 첫번째 집에 이미 설치했다고 가정
    value=array[0]
    mid=(start+end)//2

    for i in range(1,n): 
        if array[i] >= value+mid:
            count+=1
            value=array[i]
    
    # 거리를 더 늘릴 수 있는지 확인
    if count>=c:
        result=mid
        start=mid+1
    else:
        end=mid-1
print(result)

# 입력
# 5 3
# 1   
# 2
# 8
# 4
# 9



