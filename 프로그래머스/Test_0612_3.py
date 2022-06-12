def solution(n, plans, clients):
    answer = [0] * len(clients)

    plans_data=[] #요금제 정보 중 데이터 정보를 저장하기 위한 공간
    plans_service=[] #요금제 정보 중 부가서비스 정보를 저장하기 위한 공간
    for i in range(len(plans)):
        tmp=plans[i].split(' ')

        plans_data.append(int(tmp[0]))
        if i == 0:
            plans_service.append(set(tmp[1:])) 
        else:
            plans_service.append(plans_service[i-1] | set(tmp[1:])) #그 전 요금제의 부가서비스 + 추가 부가서비스

    #조건을 만족하는 요금제 찾기
    for i in range(len(clients)): 
        start=0
        end=len(plans)-1

        tmp=clients[i].split(' ')
        need_data=int(tmp[0])
        need_service=set(tmp[1:])

        while start<=end: 
            mid=(start+end)//2
            
            # 고객이 이용하는 데이터보다 요금제의 데이터가 더 크거나 고객이 이용하는 부가서비스가 요금제의 부가서비스에 포함이 안될 경우
            if need_data > plans_data[mid] or need_service.issubset(plans_service[mid])==False:
                start=mid+1
            else:
                # 현재 요금제가 기준을 만족하는 경우이므로 answer에 저장하고 더 작은 요금제 번호 찾기
                answer[i]=mid+1 
                end=mid-1
 
    return answer


print(solution(5,["100 1 3", "500 4", "2000 5"],["300 3 5", "1500 1", "100 1 3", "50 1 2"]))