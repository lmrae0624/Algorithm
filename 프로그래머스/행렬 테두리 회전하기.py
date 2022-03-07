def solution(rows, columns, queries):
    array=[[i+rows*j for i in range(1,rows+1)] for j in range(columns)]
    answer = []

    for a,b,c,d in queries:
        array[a-1][b-1]
        

    return answer


print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))