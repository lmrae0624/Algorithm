
def solution(n, wires):
    from collections import deque

    def bfs(arr):
        q=deque([arr.pop(0)])
        cnt=1

        while q:
            now, next=q.popleft()
            cnt+=1

            for a in arr:
                if now in a or next in a:
                    q.append(a)
                    arr.remove(a)
      
        return cnt

    answer = n
    for i in range(n-2,-1,-1): 
        arr=wires.copy()

        arr.pop(i)
        cnt=bfs(arr)
        answer=min(answer,abs(n-2*cnt))

    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))