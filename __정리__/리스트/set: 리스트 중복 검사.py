# 리스트에 동일 요소지만 순서가 뒤죽박죽일 경우 중복인지 확인하고 싶을 경우

# 과정1: 이런 경우 array안에 b가 없다고 판단하여 append한다
array=[[1,2,3,4]]
b=[4,3,2,1]
if b not in array:
    array.append(b)
print(array)
# [[1, 2, 3, 4], [4, 3, 2, 1]]


# 과정2: set을 이용하면 중복이라 판단하여 append하지 않음
b=[4,3,2,1]
array=[{1,2,3,4}]
b=set(b)
if b not in array:
    array.append(b)
print(array)
#[{1, 2, 3, 4}]