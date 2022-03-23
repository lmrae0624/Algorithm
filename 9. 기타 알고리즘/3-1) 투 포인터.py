# 특정한 합을 가지는 부분 연속 수열 찾기 문제 (모든 원소가 양수 데이터야함)

n, m= 5,5
data=[1,2,3,2,5]

count=0
interval_sum=0
end=0

for start in range(n):
    while interval_sum<m and end<n:
        interval_sum+=data[end]
        end+=1
    
    if interval_sum==m:
        count+=1

    interval_sum-=data[start]
    
print(count)