def solution(call):
    arr=set()
    
    max_cnt=0
    alpha_list=set(call.lower())
    for alpha in alpha_list:
        count=call.lower().count(alpha)
        if max_cnt < count:
            max_cnt=count
            arr={alpha}
        elif max_cnt==count:
            arr.add(alpha)

    for i in range(2,len(call)):
        index=0
        while index+i<=len(call):
            
            pattern=call[index:index+i].lower()
            
            count=call.lower().count(pattern)
            
            if max_cnt < count:
                max_cnt=count
                arr={pattern}
            elif max_cnt==count:
                arr.add(pattern)
            
            index+=1
    
    arr=list(arr)
    arr.sort(key=len)
    arr.reverse()

    answer=call
    for delpatt in arr:
        answer=answer.lower().replace(delpatt,"")
    
    result=''
    for c in call:
        if c.lower() in answer:
            result+=c
   
    return result


print(solution("abcabcdefabc"))
print(solution("abxdeydeabz"))
print(solution("abcabca"))
print(solution("ABCabcAb"))


