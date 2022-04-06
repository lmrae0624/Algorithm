def solution(name):
    answer = 0
    n = len(name)

    num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    def alphabet_to_num(char):
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        
        while (next_idx < n) and (name[next_idx] == 'A'): # 연속된 A의 마지막 index 찾기
            next_idx += 1
       
        distance = min(idx, n - next_idx) 
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer
    

print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("AAA"))
# print(solution("AABAB"))
print(solution("ABAAAAAAAAABB"))