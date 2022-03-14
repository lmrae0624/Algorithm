def solution(n):
    count=bin(n)[2:].count('1')

    while True:
        n+=1
        tmp=bin(n)[2:].count('1')
        if count==tmp:
            break

    return n

print(solution(78))
print(solution(15))