def solution(record):
    answer = []
    id_nick_list={}

    for r in record:
        new_list=r.split()
        if new_list[0]!='Leave':
            id_nick_list[new_list[1]]=new_list[2]
    
    for r in record:
        new_list=r.split()
        if new_list[0]=='Enter':
            answer.append(id_nick_list[new_list[1]]+'님이 들어왔습니다.')
        if new_list[0]=='Leave':
            answer.append(id_nick_list[new_list[1]]+'님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))



def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer