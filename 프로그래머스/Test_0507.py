def solution(survey, choices):
    type={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0} #지표별로 점수 저장할 공간
    score={1:3, 2:2, 3:1, 5:1, 6:2, 7:3} #선택지에 따른 점수

    # 선택에 따른 각 지표별 점수 할당
    for i in range(len(choices)):
        if choices[i]==4:
            continue
        
        
        if choices[i]<4:
            type[survey[i][0]]+=score[choices[i]]
        else:
            type[survey[i][1]]+=score[choices[i]]

    # 점수가 높은 지표 판별
    answer = ''
    order=[['R','T'],['C','F'],['J','M'],['A','N']]
    for i in range(4):
        if type[order[i][0]] >= type[order[i][1]]:
            answer+=order[i][0]
        else:
            answer+=order[i][1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))