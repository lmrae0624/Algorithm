
def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []

    array=[[] for _ in range(num_teams+1)]
    for i in range(len(employees)):
        tmp=list(employees[i].split()) # 팀 별로 사원 넣기 위해 split
        array[int(tmp[0])].append([i+1,tmp[1:]]) #해당 팀번호에 [사원번호, 해당 업무] append

    for i in range(1,len(array)): # 팀번호
        count=0 #팀의 모든 사원이 재택인지 확인용
        for j in range(len(array[i])): # 해당 팀의 사원
            if not any(a in office_tasks for a in array[i][j][1]): #업무중에 하나라도 office업무면 True 모두 재택이면 False
                count+=1 #재택 사원 한명 추가
                answer.append(array[i][j][0]) #재택 사원 번호 append
            if count==len(array[i]): #팀 인원수랑 재택 인원이 같을 경우 사원번호가 가장 작은 사원 pop
                answer.pop(-count)

    return answer

print(solution(3,["development","marketing","hometask"],["recruitment","education","officetask"],["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]))