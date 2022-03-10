#접두사 합(prefix sum): 리스트의 맨 앞부터 특정 위치까지의 합을 구해 놓은 것
from dbm import dumb
from sys import prefix


n=5
data=[10,20,30,40,50]

sum_value=0
prefix_sum=[0]
for i in data:
    sum_value+=i
    prefix_sum.append(sum_value)

left, right = 3, 4
print(prefix_sum[right]-prefix_sum[left-1])