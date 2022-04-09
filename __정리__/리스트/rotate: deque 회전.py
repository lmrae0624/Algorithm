from collections import deque
items = deque([1, 2])
items.rotate(1)     #[3, 1, 2]
items.rotate(-1)    #[1, 2, 3]