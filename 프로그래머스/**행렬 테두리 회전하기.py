def solution(rows, columns, queries):
    answer = []
        
    graph=[[j for j in range(i*columns+1,(i+1)*columns+1)] for i in range(rows)]
    #[[i+j*columns for i in range(1,columns+1)] for j in range(rows)]
    
    for x1,y1,x2,y2 in queries:
        x1-=1
        y1-=1
        x2-=1
        y2-=1
        x, y= x1, y1
        
        before=graph[x][y]
        tmp=[before]

        while y < y2:
            y+=1
            graph[x][y],before=before,graph[x][y]
            tmp.append(before)
        
        while x < x2:
            x+=1
            graph[x][y],before=before,graph[x][y]
            tmp.append(before)
        
        while y > y1:
            y-=1
            graph[x][y],before=before,graph[x][y]
            tmp.append(before)
        
        while x > x1:
            x-=1
            graph[x][y],before=before,graph[x][y]
            tmp.append(before)
        
        answer.append(min(tmp))

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))