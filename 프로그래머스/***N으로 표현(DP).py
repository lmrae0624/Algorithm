def solution(N, number):
    answer = -1
    dp=[]

    for i in range(1,9): #i는 N의 개수이고 최솟값이 8보다 크면 -1 리턴하기 때문에 1부터 9까지 반복

        array=set()
        array.add(int(str(N)*i))

        for j in range(0,i-1): # i가 5일 경우 j는 마지막을 제외한 0,1,2,3까지 돌고
            for x in dp[j]: #dp[0](N 1개로 만들 수 있는 숫자)을 또 반복       dp[0] d[1] dp[2] dp[3]
                for y in dp[-j-1]: #dp[-1](N 4개로 만들 수 있는 숫자)을 반복  dp[-1] d[-2] dp[-3] dp[-4]
                    array.add(x+y)
                    array.add(x-y)
                    array.add(x*y)

                    if y!=0:
                        array.add(x//y)

        if number in array:
            answer=i
            break

        dp.append(array)

    return answer


print(solution(5,12))