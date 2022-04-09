def solution(tstring, variables):
    arr=list(map(str,tstring.split()))
    
    new_variable={i:j for i,j in variables}

    def check(first, word):
        if word[1:-1] not in new_variable:
            return word
            
        change=new_variable[word[1:-1]]
        if change.isalpha():
            return change
        else:
            if first==change or change[1:-1] not in new_variable:
                return change
            return check(first,change)
  

    for i in range(len(arr)):
        if arr[i][0]=="{" and arr[i][-1]=='}':
            arr[i]=check(arr[i],arr[i])
    
    return " ".join(arr)


print(solution("this is {template} {template} is {state}",[["template", "{state}"], ["state", "{templates}"]]))
print(solution("{a} {b} {c} {d} {i}",[["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]))