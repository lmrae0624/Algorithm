n, m, k=map(int,input().split())
array=list(map(int,input().split()))
array.sort(reverse=True)

count=m//(k+1)*k
count+=m%(k+1)

result = array[0]*count + array[1]*(m-count)

print(result)

# 5 8 3
# 2 4 5 4 6