# 무방향에서만 판별이 가능하다

def find_parent(parent,x): #루트 노드 찾기
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


v, e=map(int,input().split()) #노드, 간선(union 연산)
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i

cycle=False
for i in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b): # a,b의 루트 노드를 찾아서 비교해서 같으면 사이클 발생
        cycle=True
        break
    else: # 같지 않으면 union 연산 수행 
        union_parent(parent,a,b)

if cycle:
    print('사이클 발생')
else:
    print('사이클 발생x')

# 3 3 
# 1 2 
# 1 3
# 2 3
