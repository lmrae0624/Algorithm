def solution(user_id, banned_id):
    from itertools import permutations 
    def check(users,banned_id):
        for i in range(len(banned_id)):
            if len(users[i])!=len(banned_id[i]):
                return False

            for j in range(len(users[i])):
                if banned_id[i][j]=="*":
                    continue
                
                if users[i][j]!=banned_id[i][j]:
                    return False
        return True
    
    answer=[]
    for users in permutations(user_id,len(banned_id)):
        if check(users,banned_id) :
            users=set(users) # 비교할 리스트를 set으로 바꾸면 비교당할 리스트에서 중복을 검색할 수 있음
            if users not in answer:
                answer.append(users)
        
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))