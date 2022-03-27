def solution(sentences, n):
    from itertools import combinations 
    answer = 0
    array=['shift'] 
    for sen in sentences:
        sen=sen.replace(" ","") #스페이스 외 문자 확인하기 위해 공백 제거
        sen=sen.lower() 
        for s in set(sen): #모든 문자 소문자로 변환하여 없는 값들만 array에 append
            if s not in array:
                array.append(s)
    
    def check(sentences,key): #점수 체크 함수
        score=0
        for sen in sentences: #각 문장 확인
            cnt=0
            cnt+=sen.count(' ') #공백만큼 점수 더하기
            sen=sen.replace(" ","")

            for s in sen: #문장내 문자열 하나씩 확인
                if s.isupper(): #대문자일 경우
                    if ('shift' not in key) or (s.lower() not in key): #shift나 소문자가 key안에 없을 때 해당 문자를 못만들기 때문에 break
                        cnt=0
                        break
                elif s not in key: #소문자의 경우 key에 없으면 break
                    cnt=0
                    break
            
                if s.isupper(): #대문자면 2점 점수 추가
                    cnt+=2
                else: #소문자일 경우 1점 점수 추가
                    cnt+=1
            score+=cnt
        return score

    for key in list(combinations(array, n)): #key 조합
        answer=max(answer,check(sentences,key)) 


    return answer

print(solution(["line in line", "LINE", "in lion"],5))