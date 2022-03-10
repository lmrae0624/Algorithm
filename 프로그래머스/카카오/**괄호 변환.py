def count(string):
    count=0
    for i in range(len(string)):
        if string[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return i

def right(p):
    count=0
    for i in p:
        if i == '(':
            count+=1
        else:
            if count==0:
                return False
            count-=1
    return True

def solution(p):
    answer = ''
    if p=='':
        return answer

    index=count(p)
    u=p[:index+1]
    v=p[index+1:]

    if right(u):
        answer+=u+solution(v)
    else:
        tmp='('+solution(v)+')'
        for s in u[1:-1]:
            if s=='(':
                tmp+=')'
            else:
                tmp+='('
        answer+=tmp

    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))(())(("))


# 이거는 동일하게 맞음
def right(string):
    if string[0]=='(' and string[-1]==')':
        return True
    else: 
        return False

# 이 함수가 틀림
def solution(p):
    answer = ''
    v=p
    if len(p)==0:
        return answer

    while True:
        index=count(v)
        u=v[:index+1]
        v=v[index+1:]
        
        if right(u):
            answer+=u
        else:
            tmp='('+v+')' #틀림
            for s in u[1:-1]:
                if s=='(':
                    tmp+=')'
                else:
                    tmp+='('
            answer+=tmp
        
        if len(p)==len(answer):
            break

    return answer

def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
