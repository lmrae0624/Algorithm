def solution(str1, str2):
    array1,array2=[],[]
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            array1.append(str1[i:i+2].lower())

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            array2.append(str2[i:i+2].lower())

    inter=[]
    arr1=array1.copy()
    for a in array2:
        if a in arr1:
            inter.append(a)
            arr1.remove(a)

    union=len(array1)+len(array2)-len(inter)

    return int(len(inter)/union*65536) if union!=0 else 0 if inter else 65536

print(solution("FRANCE","french"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))
print(solution("A+C","DEF"))


import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)