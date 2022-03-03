sym="~!@#$%^&*()=+[{]}:?,<>/"

def solution(new_id):
    new_id=new_id.lower()
    new_id=''.join( x for x in new_id if x not in sym)
    
    answer = ''
    count=0
    for i in new_id:
        if i=='.':
            count+=1
        else:
            count=0

        if count<=1:
            answer+=i

    answer=answer.strip('.')

    if answer=='':
        answer+='a'

    if len(answer)>=16:
        answer=answer[:15]

    answer=answer.rstrip('.')

    while len(answer)<=2:
        answer+=answer[-1]  
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))


# 정규식 코드
import re

def solution(new_id):
    st = new_id
    st = st.lower() 
    st = re.sub('[^a-z0-9\-_.]', '', st) 
    st = re.sub('\.+', '.', st) 
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st