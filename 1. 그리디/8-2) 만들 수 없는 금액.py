n=int(input())
array=list(map(int,input().split()))
array.sort()

result=1
for a in array:
    if result < a:
        break
    
    result+=a


print(result)


# 5
# 3 2 1 1 9
