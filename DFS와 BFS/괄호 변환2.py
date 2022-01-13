p=input()

def index_find(x):
    index=0
    for i in range(len(x)):
        if x[i]=='(':
            index+=1
        else:
            index-=1

        if index==0:
            return i
    return 

def check(x):
    count=0
    for i in range(len(x)):
        if p[i]=='(':
            count+=1
        else:
            if count==0:
                return False
            count-=1
    return True

def solution(x):
    answer=''

    if x=='':
        return answer

    index=index_find(x)+1
    u=x[:index]
    v=x[index:]

    if check(u):
        answer+=u
        answer+=solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'

        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]=='(': 
                u[i]=')'
            else:
                u[i]='('
       
        answer+="".join(u)
    return answer

print(solution(p))

