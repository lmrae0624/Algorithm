def solution(s):
    turn=0
    count=0
    
    while s!='1':
        turn+=1
        count+=s.count('0')
        s=bin(s.count('1'))[2:]

    return [turn,count]

print(solution("110010101001"))