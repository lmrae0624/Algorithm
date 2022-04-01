num=list(map(int,input().split()))
plus,minus,multi,div=map(int,input().split())
len=len(num)

max_result=-int(1e9)
min_result=int(1e9)

def dfs(index,x):
    global max_result,min_result,plus,minus,multi,div
    
    if index==len:
        max_result=max(max_result,x)
        min_result=min(min_result,x)
        return  

    if plus>0:
        plus-=1
        dfs(index+1,x+num[index])
        plus+=1
    if minus>0:
        minus-=1
        dfs(index+1,x-num[index])
        minus+=1
    if multi>0:
        multi-=1
        dfs(index+1,x*num[index])
        multi+=1
    if div>0:
        div-=1
        dfs(index+1,int(x/num[index]))
        div+=1

dfs(1,num[0])
print(max_result,min_result)

print(int(-7/3))
# 1 2 3 4 5 6
# 2 1 1 1