def solution(nums):
    answer = 0
    count=len(nums)//2
    nums=set(nums)

    if count>len(nums):
        answer=len(nums)
    else:
        answer=count
    return answer

print(solution([3,1,2,3]))


def solution(ls):
    return min(len(ls)/2, len(set(ls)))