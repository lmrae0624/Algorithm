def solution(record):
    answer = []

    id_nick=dict()

    for re in record:
        tmp=re.split()
        
        if tmp[0]=="Leave":
            continue

        id_nick[tmp[1]]=tmp[2]
    
    for re in record:
        tmp=re.split()
        if tmp[0]=="Change":
            continue
        
        if tmp[0]=="Enter":
            answer.append(id_nick[tmp[1]]+"님이 들어왔습니다.")
        else:
            answer.append(id_nick[tmp[1]]+"님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))