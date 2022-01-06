from bisect import bisect_left,bisect_right
n, x=map(int,input().split())
array=list(map(int,input().split()))

left_range=right_range=x
left_index=bisect_left(array, left_range)
right_index=bisect_right(array, right_range)

answer=right_index-left_index
print(-1 if answer==0 else answer)


# 입력
# 7 2
# 1 1 2 2 2 2 3