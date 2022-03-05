def solution(s):
    answer = s

    for i in range(1,len(s)//2+1): #자르는 개수 
        index=0 #시작 인덱스 

        pre_s=s[index:index+i] #이전값 저장
        count=1

        tmp=''
        while True:
            index+=i

            if pre_s==s[index:index+i]:
                count+=1
            else:
                if count>1:
                    tmp+=str(count)+pre_s
                else:
                    tmp+=pre_s
                count=1
                pre_s=s[index:index+i]

            if index+i>len(s):
                tmp+=s[index:]
                break

        if len(answer)>len(tmp):
            answer=tmp

    return len(answer)



print(solution("aabbaccc"))