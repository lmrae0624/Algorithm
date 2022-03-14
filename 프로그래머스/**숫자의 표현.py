def solution(n):
    answer = 0
    array=[]
    for i in range(1,n+1):
            
        array.append(i)
        
        while sum(array)>=n:
            if sum(array)==n:
                answer+=1
            array.pop(0)
 
    return answer

print(solution(15))