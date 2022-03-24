def solution(triangle):

    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])): #i+1로도 표현 가능
            left,right=0,0

            if j > 0:
                left=triangle[i][j]+triangle[i-1][j-1]

            if j < len(triangle[i-1]):
                right=triangle[i][j]+triangle[i-1][j]
            
            triangle[i][j]=max(left,right)

    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


def solution(triangle):
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])