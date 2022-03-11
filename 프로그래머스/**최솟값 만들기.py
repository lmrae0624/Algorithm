
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()

    alist=A.copy()
    blist=B.copy()

    while alist:
        answer+=alist.pop(0)*blist.pop(-1)
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    tmp=0
    while A:
        tmp+=A.pop(-1)*B.pop()
        
    return min(answer,tmp)


print(solution([1, 4, 2],[1, 4, 2]))
print(solution([1, 2],[3, 4]))

def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))