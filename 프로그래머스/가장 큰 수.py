def solution(numbers):
    tmp=list(map(str,numbers))

    tmp.sort(key=lambda x: x * 3, reverse=True) #각 숫자가 1000이하라는게 힌트 !
    # x*3은 문자열을 3번 곱하는 것이므로 "1"이면 "111"이 반환되고 "37"이면 "373737"이 반환된다.
    # 숫자 정렬이 아니라 문자열 정렬이기 때문에 "111" > "101010" > "100100100"> "100010001000" 

    return str(int(''.join(tmp)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([1, 10, 100, 1000]))
print(solution([10,111]))


import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer