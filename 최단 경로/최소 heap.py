import heapq

def heapsort(iterable):
    h=[]
    result=[]
    for i in iterable:
        heapq.heappush(h,i)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result=heapsort([1,0,2,7,4,3,5,6])
print(result)