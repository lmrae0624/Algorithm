# list = stack

# pop(index)
a = [1,2,1,3,4,5,1]
removed = a.pop(1)
print(a) # [1, 1, 3, 4, 5, 1] 
print(removed) # 2 


# del
a = [1,2,1,3,4,5,1] 
del a[1]
print(a) # [1, 1, 3, 4, 5, 1] 


# 제일 마지막에 넣은 값 삭제
array=[1,2,3,4]
array.pop()
# 1, 2, 3


## 뒤에서부터 삭제 
array=[1,2,3,4]
del array[-2:]
# 1, 2

array=[1,2,3,4]
array.pop(-1) # = array.pop()
# 1, 2, 3