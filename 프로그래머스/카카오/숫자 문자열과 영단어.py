
array=['zero','one','two','three','four','five','six','seven','eight','nine']

def solution1(s):
    for i in range(len(array)):
        s=s.replace(array[i],str(i))
        
    return int(s)

def solution(s):
    answer=''
    tmp=''
    for i in s:
        if i.isdigit():
            answer+=i
            continue
        
        tmp+=i
        if tmp in array:
            answer+=str(array.index(tmp))
            tmp=''
    return int(answer)
 

print(solution("one4oneseveneight"))
print(solution("1zerotwozero3"))
print(solution("1zerozero"))


num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


