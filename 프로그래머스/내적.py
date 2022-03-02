a=list(map(int,input().split(',')))
b=list(map(int,input().split(',')))

answer=sum(i*j for i,j in zip(a,b))
print(answer)

# 1,2,3,4
# -3,-1,0,2