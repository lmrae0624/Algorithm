# sort(reverse=True)는 오름차순 또는 내림차순 정렬

# reverse: 리스트 순서 자체를 뒤집기
list = [0,10,20,40]
list.reverse()
print(list)
# [40, 20, 10, 0]

# reversed
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))
# [5, 3, 4, 2, 1]
 
array=[0, 10, 20, 40]
for i in reversed(array):
    print(i)

