def solution(n, k, cmd):
    import heapq
    left=[]
    right=[]
    del_list=[]
    for i in range(n):
        heapq.heappush(right,i)
    
    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right))
    
    for c in cmd:
        if len(c)>1:
            act,num=c.split()
            if act=="D":
                for _ in range(int(num)):
                    heapq.heappush(left, -heapq.heappop(right))
            elif act=="U":
                for _ in range(int(num)):
                    heapq.heappush(right, -heapq.heappop(left))
        else:
            if c[0]=="C":
                del_list.append(heapq.heappop(right))
                
                if not right:
                    heapq.heappush(right, -heapq.heappop(left))
            else:
                tmp=del_list.pop()
                
                if tmp < right[0]:
                    heapq.heappush(left, -tmp)
                else:
                    heapq.heappush(right, tmp)

    answer=['O']*n
    for i in del_list:
        answer[i]='X'

    return "".join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))