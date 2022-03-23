# 퀵 정렬: 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다

array=[7,5,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    
    while left<=right:
        while left<=end and array[left]<=array[pivot]: #pivot보다 큰 값 찾기
            left+=1
        while right>start and array[right]>=array[pivot]: #pivot보다 작은 값 찾기
            right-=1

        if left > right: # left랑 right 교차 됐을 때 pivot이랑 작은 값(right) 교체 
            array[pivot], array[right] = array[right], array[pivot]
        else: # left(큰 값)이랑 right(작은 값) 교체
            array[left], array[right] = array[right], array[left]

    quick_sort(array,start,right-1)
    quick_sort(array,left,end)

quick_sort(array,0,len(array)-1)
print(array)
        

