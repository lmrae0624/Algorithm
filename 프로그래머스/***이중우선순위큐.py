import heapq
def solution(operations):
    answer = []
    answer_max=[]

    for oper in operations:
        a,b=oper.split()

        b=int(b)
        if a=='I':
            heapq.heappush(answer,b)
            heapq.heappush(answer_max,-b)
        elif a=='D':
            if not answer:
                continue

            if b==1: #최대값 삭제
                answer.remove(-heapq.heappop(answer_max))
            else: #최소값 삭제
                answer_max.remove(-heapq.heappop(answer))
    
    if not answer:
        return [0,0]
    else:
        return [max(answer),min(answer)]


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

heap=[1,2,3,4,5]
heap = heapq.nlargest(len(heap), heap)[1:] #최대값 삭제
heapq.heapify(heap)
print(heap)
# [1, 3, 2, 4]