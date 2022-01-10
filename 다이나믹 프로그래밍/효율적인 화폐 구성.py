n, m=map(int,input().split())
coin=[]
d=[10001]*10001

for _ in range(n):
    coin.append(int(input()))

d[0]=0
for i in range(1,m+1):
    for c in coin:
        if i>=c :
            d[i]=min(d[i],d[i-c]+1)

# 반복문의 범위를 줄일 수 있음
for i in range(n): 
    for j in range(coin[i], m + 1):
        if d[j - coin[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - coin[i]] + 1)

print(-1 if d[m]==10001 else d[m])



# 2 15
# 2
# 3

# 3 4
# 3
# 5
# 7