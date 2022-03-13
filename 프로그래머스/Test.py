def func(array,x,y,answer):
    for a in array:
        if x==a[0] and y!=a[1]:
            func(array,a[1],a[0],answer+1)
            
    return answer

def solution(n, edges):
    answer = 0

    array=[]
    for ed in edges:
        array.append(ed)
        array.append([ed[1],ed[0]])
    
    for a in array:
        for b in array:
            if a[1]==b[0] and a[0]!=b[1]:
                answer=func(array,b[1],b[0],answer+1)
    
    return answer*2

print(solution(5,[[0,1],[0,2],[1,3],[1,4]]))
print(solution(4,[[2, 3], [0, 1], [1, 2]]))