# nlargest:가장 큰 n개의 아이템 찾기
# nsmallest:가장 작은 n개의 아이템 찾기
import heapq

nums = [1, 8, 3, -5, 4, 99, -4, 0]

print(heapq.nlargest(3, nums)) 
# [99, 8, 4]
print(heapq.nsmallest(3, nums)) 
# [-5, -4, 0]


heap=[1,2,3,4,5]
heap = heapq.nlargest(len(heap), heap)[1:] #최대값 삭제
heapq.heapify(heap)
print(heap)
# [1, 3, 2, 4]