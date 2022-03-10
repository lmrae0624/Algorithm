
#재귀에서 런타임 에러, 효율성도 떨어짐
# def solution(s):
#     answer=0

#     if len(s)==0:
#         return 1
#     else:
#         pre=s[0]
#         for i in range(1,len(s)):
#             if pre==s[i]:
#                 s=s.replace(pre+pre,'',1)
#                 answer=solution(s)
#                 break
#             else:
#                 pre=s[i]

#     return answer

def solution(s):
    answer=0

    if len(s)==0:
        answer=1
    else:
        array=[s[0]]
        for string in s[1:]:
            if array:
                pre=array[-1]
                if pre==string:
                    array.pop()
                else:
                    array.append(string)
            else:
                array.append(string)             
        if not array:
            answer=1

    return answer

print(solution('a'))

def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)