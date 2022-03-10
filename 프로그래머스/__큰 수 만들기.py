def solution(number, k):
    answer = [number[0]]

    for num in number[1:]:
        while answer and k>0 and answer[-1]<num:
            answer.pop()
            k-=1
        answer.append(num)

    return "".join(answer[:len(answer)-k])

print(solution("1943",2))
print(solution("1231234",3))
print(solution("4177252841",4))