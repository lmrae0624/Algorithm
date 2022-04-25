def solution(user_id, banned_id):
    from itertools import permutations
    answer = []
    
    def check(user,banned_id):
        for i in range(len(banned_id)):
            if len(user[i])!= len(banned_id[i]):
                return False
          
            for l in range(len(user[i])):
                if banned_id[i][l]=="*":
                    continue
                
                if banned_id[i][l]!=user[i][l]:
                    return False
        return True
    
    for user in permutations(user_id,len(banned_id)):
        if check(user,banned_id):
            user=set(user)
            if user not in answer:
                answer.append(user)
    
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))