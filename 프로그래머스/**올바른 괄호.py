def solution(s):
    if s[0]==')' or s[-1]=='(':
        return False

    count=0
    for i in s:
        if i=='(':
            count+=1
        else:
            count-=1
        if count<0:
            return False

    return True if count==0 else False

print(solution("())()(()"))