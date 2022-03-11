def solution(skill, skill_trees):
    answer = len(skill_trees)

    for ski in skill_trees:
        skill_seq=list(skill)
       
        for s in list(ski):
            if s in skill_seq :
                if s==skill_seq[0]:
                    skill_seq.pop(0)
                else:
                    answer-=1
                    break

    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))


def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer