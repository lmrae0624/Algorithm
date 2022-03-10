# list(stack)보다 deque이 빠르다
def solution(people, limit):
    answer = 1
    people.sort(reverse=True)

    weight=0

    for p in people:
        weight+=p

        if weight>limit:
            answer+=1
            weight=p
        
        if len(people)==1:
            break

        if weight+people[-1]<=limit:
            weight+=people.pop(-1)
        
    return answer

print(solution([70, 50, 80, 50],100))
print(solution([70, 50,50, 20],100))
print(solution([10,20,70,70],100))
print(solution([100,500,500,900,950],1000))

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
