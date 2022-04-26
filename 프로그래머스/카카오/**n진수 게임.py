def solution(n, t, m, p):
    answer = ''

    def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base) 
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

    arr=[]
    num=0
    while len(arr)<=t*m:
        arr.extend(convert(num,n))
        num+=1

    for i in range(p-1, t*m, m):
        answer += arr[i]

    return answer

print(solution(2,4,2,1))


