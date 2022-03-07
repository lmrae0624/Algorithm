#collections.Counter(a) : a에서 요소들의 개수를 세어, 딕셔너리 형태로 반환합니다.  {문자 : 개수} 형태

import collections

b = [1,3,4,2,3,5,2,3,9]
a = [1,2,3,4,1,5,3,1,3,4,2,3]
print(collections.Counter(a) , collections.Counter(b))
# Counter({3: 4, 1: 3, 2: 2, 4: 2, 5: 1}) Counter({3: 3, 2: 2, 1: 1, 4: 1, 5: 1, 9: 1})