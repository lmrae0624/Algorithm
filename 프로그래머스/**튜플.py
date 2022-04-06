def solution(num):
    answer = []
    num=num.strip("{""}")
    num=list(num.split('},{'))

    len_list=dict()
    for n in num:
        tmp=list(n.split(','))
        len_list[len(tmp)]=tmp
    
    for i in range(1,len(num)+1):
        for j in len_list[i]:
            if int(j) not in answer:
                answer.append(int(j))
                continue

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

# 기존 코드에서 수정
def solution(s):
    answer = []
    num = s.lstrip('{').rstrip('}').split('},{')

    len_list=[]
    for n in num:
        len_list.append(n.split(','))
    
    len_list.sort(key=len)
    #[['2'], ['2', '1'], ['2', '1', '3'], ['2', '1', '3', '4']]
    
    for i in range(len(num)):
        for j in len_list[i]:
            if int(j) not in answer:
                answer.append(int(j))
                continue

    return answer

# 다른 방법: Counter로 개수세서 제일 많은 숫자부터 담으면 됨
from collections import Counter
def solution(s):
    new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
    return [int(c[0]) for c in sorted(Counter(new_s).items(), key = lambda x: x[1],reverse=True )]