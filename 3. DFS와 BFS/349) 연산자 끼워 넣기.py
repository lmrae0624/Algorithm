n=int(input())
num_list=list(map(int,input().split()))
add, sub, mul, div =list(map(int,input().split()))

min_result = 1e9
max_result = -1e9

def dfs(i,x):
    global min_result, max_result, add, sub, mul, div
    
    if i == n:
        min_result=min(min_result,x)
        max_result=max(max_result,x)
    else:
        if add>0:
            add-=1
            dfs(i+1,x+num_list[i])
            add+=1
            # dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)  이렇게도 가능
        if sub>0:
            sub-=1
            dfs(i+1,x-num_list[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,x*num_list[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,int(x/num_list[i]))
            div+=1

dfs(1,num_list[0])
print(max_result)
print(min_result)

# 2
# 5 6
# 0 0 1 0

# 3
# 3 4 5
# 1 0 1 0

# 6
# 1 2 3 4 5 6
# 2 1 1 1