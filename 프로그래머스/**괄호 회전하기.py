def solution(string):
    from collections import deque
    answer = 0

    def check(string):
        stack=[]
        for i in range(len(string)):
            if stack:
                before=stack[-1]
                if string[i]==")":
                    if before=="(":
                        stack.pop()
                        continue
                elif string[i]=="]":
                    if before=="[":
                        stack.pop()
                        continue
                elif string[i]=="}":
                    if before=="{":
                        stack.pop()
                        continue
            stack.append(string[i])

        return False if stack else True

    string = deque(list(string))
    for _ in range(len(string)):
        string.rotate(1)
        if check(string):
            answer+=1

    return answer

print(solution("[](){}"))