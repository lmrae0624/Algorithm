array=list(map(int,input().split()))
array.sort()

count,result=0,0

for i in array:
    count+=1
    if count>=i:
        result+=1
        count=0

print(result)


# 2 3 1 2 2
# =2