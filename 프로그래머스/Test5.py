def solution(histogram):
    answer=0
    
    a,b=0,len(histogram)-1

    while a < b:
        h=min(histogram[a],histogram[b])
        x=abs(a-b)-1

        answer=max(answer,h*x)

        if histogram[a]>histogram[b]:
            b-=1
        else :
            a+=1

    return answer

print(solution([2,2,2,3]))
print(solution([6,5,7,3,4,2]))
print(solution([3,10,1,10,3]))