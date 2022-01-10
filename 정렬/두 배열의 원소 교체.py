n, k=map(int,input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

alist.sort()
blist.sort()

for i in range(k):
    alist[i], blist[n-1-i] = blist[n-1-i], alist[i]

print(sum(alist))

alist.sort() # 배열 A는 오름차순 정렬 수행
blist.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if alist[i] < blist[i]:
        # 두 원소를 교체
        alist[i], blist[i] = blist[i], alist[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

# 입력
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5