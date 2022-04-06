rows=5
columns=3
  
graph=[[j for j in range(i*columns+1,(i+1)*columns+1)] for i in range(rows)]
print(graph)
#[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

graph=[[i+j*columns for i in range(1,columns+1)] for j in range(rows)]
print(graph)
#[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]