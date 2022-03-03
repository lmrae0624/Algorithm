import re

def solution(new_id):
    st = new_id
    st = st.lower() # 소문자로
    st = re.sub('[^a-z0-9\-_.]', '', st) # 정규식 조건에 없는건 ''로 변환
    st = re.sub('\.+', '.', st) #.이 한개 이상 반복되면 .으로 변환
    st = re.sub('^[.]|[.]$', '', st) # 앞뒤로 . 있으면 ''로 변환
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st) # 앞뒤로 . 있으면 ''로 변환
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

# (*): ct=Yes ("a"가 0번 반복되어 매치반복)
# (+): ct=No ("a"가 0번 반복되어 매치되지 않음) :1번 이상
# ^: 이 패턴으로 시작해야 함
# $: 이 패턴으로 종료되어야 함
#[^문자들]: [문자들]의 반대로 피해야할 문자들의 집합을 정의함 (not)
#| :두 패턴 중 하나이어야 함 (OR 기능)

