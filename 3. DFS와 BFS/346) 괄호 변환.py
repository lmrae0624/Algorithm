p=input()

def index_find(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return i

def check(p):
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
    answer=''
    if p=='':
        return answer

    i=index_find(p)+1
    u=p[:i]
    v=p[i:]

    if check(u):
        answer=u+solution(v)
    else:
        answer='('
        answer+=solution(v)
        answer+=')'

        tmp=list(u[1:-1])
        for i in range(len(tmp)):
            if tmp[i]=='(':
                tmp[i]=')'
            else:
                tmp[i]='('
        answer+="".join(tmp) #구분자'.join(리스트)
    return answer

print(solution(p))
