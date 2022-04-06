# 시간초과 코드
def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)

    def cul(name,total):
        if name=='-' or total<1:
            return
        idx=enroll.index(name) #index하면 시간 초과하기 때문에 dict쓰기
        
        share=total//10
        answer[idx]+=(total-share)
       
        cul(referral[idx],share)
    
    for i in range(len(seller)):
        cul(seller[i],amount[i]*100)

    return answer

# 새로 작성한 코드
def solution(enroll, referral, seller, amount):
    answer = {enroll[i]:0 for i in range(len(enroll))}
    ref = {enroll[i]:referral[i] for i in range(len(enroll))}

    def cul(name,total):
        if name=='-' or total<1:
            return
        
        share=total//10
        answer[name]+=(total-share)
       
        cul(ref[name],share)
    
    for i in range(len(seller)):
        cul(seller[i],amount[i]*100)

    return list(answer.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],
[12, 4, 2, 5, 10]))