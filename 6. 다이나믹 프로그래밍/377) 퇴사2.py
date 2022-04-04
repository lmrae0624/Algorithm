n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

dp=[0]*n

for i in range(n):
    for j in range(i):
        if i>=array[j][0]+j:
            dp[i]=max(dp[i],dp[j])

    if array[i][0]+i<=n:
        dp[i]+=array[i][1]

print(dp)
print(max(dp))


# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10