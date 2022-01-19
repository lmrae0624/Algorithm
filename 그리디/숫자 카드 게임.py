n, m= map(int,input().split())
result=0

for i in range(n):
    tmp=list(map(int,input().split()))
    result=max(min(tmp),result)

print(result)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4