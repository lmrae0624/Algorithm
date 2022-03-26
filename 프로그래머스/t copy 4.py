def solution(arr, brr):
    answer = 0

    for i in range(len(arr)-1):
        diff=brr[i]-arr[i] #원소 차이 저장

        if diff==0: #차이가 없을 경우 continue
            continue
        
        answer+=1 #셀 너비조절 횟수+1
        arr[i+1]-=diff #다음 셀의 경우 움직인 만큼 영향 받기 때문에 값 변경

    return answer

print(solution([3, 7, 2, 4],[4, 5, 5, 2]))
print(solution([6, 2, 2, 6],[4, 4, 4, 4]))


def solution(req_id, req_info):
    answer = []
    buy=[]
    sell=[]
    for i in range(len(req_id)):
        if req_info[i][0]==1:
            sell.append((req_id[i],req_info[i][1],req_info[i][2]))
        else:
            buy.append((req_id[i],req_info[i][1],req_info[i][2]))

    return answer

#print(solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"],[[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]))