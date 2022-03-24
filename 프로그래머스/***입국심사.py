def solution(n, times):
    answer = 0
    start=1
    end=max(times)*n #가장 오래걸리는 시간

    while start<=end:
        mid=(start+end)//2 #이 시간동안 심사가 가능한지 판단하기
        people=0

        for t in times: 
            people += mid // t # mid시간동안 심사 가능한 인원수 세기
        
        if people >= n: #심사 가능
            answer = mid
            end = mid - 1
        else: #심사 불가능
            start = mid + 1

    return answer

print(solution(6,[7,10]))

def solution(n, times):
    answer = 0
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid
        else:
            start = mid + 1
    answer = start
    return answer