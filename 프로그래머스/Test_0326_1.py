def solution(logs):
    answer = 0
    array=['team_name','application_name','error_level','message']

    for log in logs:
        
        if len(log)>100 : #로그의 길이는 100 이하
            answer+=1
            continue

        log=list(log.split(' '))
     
        if len(log)!=12  : # 공백 기준으로 나누고 형식의 맞는 리스트의 길이가 :과 t,a,e,m 까지 12여야함 
            answer+=1
        else:
            for i in range(12): 
                if i%3==0: # t,a,e,m가 맞는지 확인
                    if log[i] not in array:
                        answer+=1
                        break
                elif i%3==1: # :이 맞는지 확인
                    if log[i]!=":":
                        answer+=1
                        break
                else:
                    if not log[i].isalpha(): # 값이 대소문자로만 이루어졌는지 확인
                        answer+=1
                        break

    return answer


print(solution(["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]))
print(solution(["   team_name  : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))