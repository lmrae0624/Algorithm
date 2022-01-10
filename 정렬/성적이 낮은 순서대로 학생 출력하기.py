n=int(input())
array=[]
for _ in range(n):
    array.append(list(map(str,input().split())))

array = sorted(array, key=lambda student: int(student[1]))
# sorted: 비교 함수는 익명 함수(lambda) 도 가능하고, 별도로 정의 가능
# 비교할 아이템의 요소가 복수 개일 경우, 튜플로 그 순서를 내보내주면 된다. ex) sorted(e, key = lambda x : (x[0], -x[1]))

for i in range(n):
    print(array[i][0],end=' ')

# 입력
# 2
# 홍길동 95
# 이순신 77