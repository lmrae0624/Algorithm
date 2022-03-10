def solution(n):
    tmp = ''

    while n > 0:
        n, mod = divmod(n, 3)
        tmp += str(mod)

    return int(tmp,3)

print(solution(45))