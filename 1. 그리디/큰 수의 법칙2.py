n, m, k=map(int,input().split())
array=list(map(int,input().split()))
array.sort(reverse=True)

count=m//(k+1)
result = array[0]*(m-count) + array[1]*count

print(result)

# 5 8 3
# 2 4 5 4 6
# = 46
