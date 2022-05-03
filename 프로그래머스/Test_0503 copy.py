
def solution(A):
    answer=0

    switch=[0]*(len(A)+1) #스위치가 켜졌는지 여부를 확인하기 위함 0=꺼짐 1=켜짐
    light=[0]*(len(A)+1) #불이 켜졌는지 여부를 확인하기 위함 0=꺼짐 1=켜짐
    switch[0],light[0] = 1,1

    def trun_on(light,switch,a): # 뒤에 켜져야하는 불이 있나 확인
        i=1
        while a+i<len(light): 
            if switch[a+i]==1: # 다음 전구의 스위치가 눌려져 있으면 불이 켜진거로 변경
                light[a+i]=1
                i+=1
            else: 
                return 

    for a in A:
        switch[a]=1 
        
        if light[a-1]==1: #현재 위치 앞에 불이 켜져있을때 
            light[a]=1 #현재 위치의 불도 켜짐
            trun_on(light,switch,a) # 뒤에 켜져야하는 불이 있나 확인

        if sum(switch)==sum(light): # 스위치 켜진 개수와 불이 켜진 개수가 같을 때 날짜 하루 추가
            answer+=1
        
    return answer

print(solution([2,3,4,1,5]))