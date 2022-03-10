n,m = map(int,input().split())
array=list(map(int,input().split()))
array.sort()

# result=0
# count=1
# for i in range(n-1):
#     if array[i]!=array[i+1]:
#         result+=(n-i-1)*count
#         count=1
#     else:
#         count+=1

# print(result)

# 1<=m<=10에 포인트 두기

w=[0]*(m+1)
for i in array:
    w[i]+=1

result=0
for i in range(1,m+1):
    result+=sum(w[i+1:])*w[i]

print(result)

# 5 3
# 1 3 2 3 2