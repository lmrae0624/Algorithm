# 계수 정렬: 데이터의 크기 범위가 제한되어 정수 형태로 표현 할 수 있을 때만 사용 가능하지만 빠름
# 가장 큰 데이터와 가장 작은 데이터 차이가 백만을 넘지 않을 때 효과적
# 동일 값을 가지는 데이터가 여러 개 등장할 때 적합 (학생 성적 분포도)

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')