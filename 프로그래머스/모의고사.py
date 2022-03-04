plist1=[1,2,3,4,5]
plist2=[2, 1, 2, 3, 2, 4, 2, 5]
plist3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    right=[0,0,0]

    for i in range(len(answers)):
        if answers[i]==plist1[i%len(plist1)]:
            right[0]+=1
        if answers[i]==plist2[i%len(plist2)]:
            right[1]+=1
        if answers[i]==plist3[i%len(plist3)]:
            right[2]+=1
 
    result=max(right)
    for i in range(3):
        if result==right[i]:
            answer.append(i+1)

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))


def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
