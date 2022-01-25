n,m=map(int,input().split())
max_value=0

for i in range(n):
    tmp=list(map(int,input().split()))
    max_value=max(min(tmp),max_value)

print(max_value)


# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# =2