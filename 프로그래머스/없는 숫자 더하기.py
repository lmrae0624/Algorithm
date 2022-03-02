numbers=list(map(int,input().split(',')))
num_list=[0,1,2,3,4,5,6,7,8,9]
answer=0

for n in num_list:
    if n not in numbers:
        answer+=n
print(answer)

def solution(numbers):
    return 45 - sum(numbers)

# 1,2,3,4,6,7,8,0
# 5,8,4,0,6,7,9