import heapq

def sortheap(iterable):
    h=[]
    result=[]
    for i in iterable:
        heapq.heappush(h,-i)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result=sortheap([1,0,2,7,4,5,6])
print(result)