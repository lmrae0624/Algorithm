def solution(word):
    alpha=['A', 'E', 'I', 'O', 'U']

    word_list=[]
    def dfs(w):
        if w==word:
            return True

        if len(w)>=5:
            return

        for a in alpha:
            word_list.append(w+a)
            if dfs(w+a):
                return True
                
    for a in alpha:
        word_list.append(a)
        if dfs(a):
            break
    
    return len(word_list)

print(solution("AAAAE"))
print(solution("I"))