n=int(input())
number=list(map(int,input().split()))
plus, minus, mult, div=map(int,input().split())

min_result=(1e9)
max_result=-(1e9)

def dfs(index,x):
    global plus, minus, mult, div, min_result, max_result

    if index==n:
        max_result=max(max_result,x)
        min_result=min(min_result,x)

    if plus>0:
        plus-=1
        dfs(index+1,x+number[index])
        plus+=1
    if minus>0:
        minus-=1
        dfs(index+1,x-number[index])
        minus+=1
    if mult>0:
        mult-=1
        dfs(index+1,x*number[index])
        mult+=1
    if div>0:
        div-=1
        dfs(index+1,int(x/number[index]))
        div+=1
    

dfs(1,number[0])
print(max_result)
print(min_result)