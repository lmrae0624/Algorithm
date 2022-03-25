def solution(n, costs):
    answer = 0
   
    def find_parent(parent,x):
        if parent[x]!=x:
            parent[x]=find_parent(parent,parent[x])
        return parent[x]

    def union_parent(parent,a,b):
        a=find_parent(parent,a)
        b=find_parent(parent,b)
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
 
    parent = [0] * n
    for i in range(1,n):
        parent[i]=i

    array=[]
    for cost in costs:
        array.append((cost[2],cost[0],cost[1]))

    array.sort()

    for a in array:
        cost,x,y=a

        if find_parent(parent,x) != find_parent(parent,y): #루트노드가 같다면 사이클 발생
            union_parent(parent,x,y)
            answer+=cost

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))


