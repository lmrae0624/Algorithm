def solution(people, limit):
    answer = 0

    people.sort() 
    total=0 
    for p in people:
        total+=p
        
        if total>limit:
            total=p
            answer+=1
        print(total)

    return answer+1

print(solution([70, 50, 80, 50],100))
print(solution([70, 50, 80],100))
