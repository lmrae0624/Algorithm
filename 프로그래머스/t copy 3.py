def solution(abilities, k):
    answer = 0
    abilities.sort(reverse=True) # 능력치 내림차순
    
    diff=[] # 새로운 팀원을 데리고 올때 차이가 큰 순서에 우선권을 쓰기 위해 능력치 차이를 저장할 list생성

    for i in range(0,len(abilities),2): #한 라운드당 1명씩(총 2명) 능력치를 한번에 확인하기 때문에 step을 2로 설정
        if i==len(abilities)-1: # 홀수 인원일 경우 마지막엔 내가 데려가는 사람이 없기 때문에 그대로 abilities[i]가 능력치 차이
            diff.append(abilities[i])
        else:
            diff.append(abilities[i]-abilities[i+1]) # 그외의 경우 i사람과 i+1의 능력치 차이를 append
        answer+=abilities[i+1]  #우선권을 쓰지 않을 경우 내가 가져가는 총 능력치 

    for i in range(k):  # 우선권 쓰기
        find = diff.index(max(diff)) # diff(차이 리스트)에서 가장 큰 값의 index를 find로 저장
       
        if find*2+1!=len(abilities):
            answer-=abilities[find*2+1] # 원래 데려갔던 사람의 능력치 빼고
        answer+=abilities[find*2] # 능력치가 더좋은 앞사람 데려가기
        diff[find]=0 #해당값은 이미 처리했기때문에 0으로 새로 설정

    return answer

print(solution([2, 8, 3, 6, 1, 9, 1, 9],2))
print(solution([7, 6, 8, 9, 10],1))