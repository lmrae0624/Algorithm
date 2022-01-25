n, m =map(int,input().split())
array=list(map(int,input().split()))

d=[0]*(n+1)
for i in array:
    d[i]+=1

result=0
# for i in range(1,m+1):
#     result+=sum(d[i+1:])*d[i]

for i in range(1,m+1):
    n-=d[i]
    result+=n*d[i]
    
print(result)


# 5 3
# 1 3 2 3 2