def solution(p):
    answer = [0]*len(p)

    for i in range(len(p)):
        min=i #최소값의 인덱스

        #최소값의 인덱스 찾기
        for j in range(i+1,len(p)):
            if p[min] > p[j]: 
                min=j

        #최소값의 인덱스와 현재 인덱스가 다르면 값 바꾸기
        if min != i: 
            p[i], p[min] = p[min], p[i] 

            answer[i]+=1 
            answer[min]+=1

    return answer


print(solution([2,5,3,1,4]))
print(solution([2,5,3,1,4,6]))