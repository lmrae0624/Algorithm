#enumerate(): 함수는 기본적으로 인덱스와 원소로 이루어진 터플(tuple)을 만들어줍니다.
for entry in enumerate(['A', 'B', 'C']):
    print(entry)
# (0, 'A')
# (1, 'B')
# (2, 'C')


# 인덱스를 0부터 할당하는게 아니라 1부터 할당하기
for i, letter in enumerate(['A', 'B', 'C'], start=1):
    print(entry)
# 1 A
# 2 B
# 3 C