# collections.Counter(a).most_common(n): a의 요소를 세어, 최빈값 n개를 반환합니다. (리스트에 담긴 튜플형태로)

import collections

a  = [1,1,1,2,3,2,3,245,9]
print(collections.Counter(a).most_common(3))
# [(1, 3), (2, 2), (3, 2)] =1:3개, 2:2개, 3:2개