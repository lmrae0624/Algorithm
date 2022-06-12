def solution(periods, payments, estimates):
    answer = [0, 0] #[이번 달 VIP아니지만 다음 달 VIP 고객 수, 이번 달 VIP 다음 달 VIP아닌 고객 수]

    for i in range(len(periods)):
        # 다음 달 기준 가입 기간이 2년(24개월)미만인 경우 vip가 될 수 없음
        if periods[i] < 23 : 
            continue 
        
        # 이번 달 vip인지 다음 달 vip인지 확인하기 위한 변수
        now_vip, next_vip = False, False

        now_total_payment=sum(payments[i]) # 이번 달 기준 연간 납부 금액
        if ((24 <= periods[i] < 60) and now_total_payment >= 900000) or ((periods[i] >= 60) and now_total_payment >= 600000):
            now_vip = True

        next_total_payment = now_total_payment - payments[i][0] + estimates[i] # 다음 달 기준 연간 납부 금액
        if ((24 <= periods[i]+1 < 60) and next_total_payment >= 900000) or ((periods[i]+1 >= 60) and next_total_payment >= 600000):
            next_vip = True
        
        if now_vip==False and next_vip==True:
            answer[0]+=1
        elif now_vip==True and next_vip==False:
            answer[1]+=1
        
    return answer

print(solution([20,23,24],[[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],[100000,100000,100000]))