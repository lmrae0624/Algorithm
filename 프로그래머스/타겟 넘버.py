
answer=0
def cul(numbers,target,result,index):
    global answer
    if index==len(numbers): #더 돌릴게 없을때
        if result==target:
            answer+=1
        return

    cul(numbers,target,result+numbers[index],index+1)
    cul(numbers,target,result-numbers[index],index+1)
    

def solution(numbers, target):
    global answer
    answer=0
    result=0

    cul(numbers,target,result+numbers[0],1)
    cul(numbers,target,result-numbers[0],1)

    return answer

print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])