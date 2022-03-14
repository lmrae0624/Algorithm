def solution(s):
    answer = ''
    array=list(map(int,s.split()))
    answer+=str(min(array))+' '+str(max(array))
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))