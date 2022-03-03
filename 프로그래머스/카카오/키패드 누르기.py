keypad=[[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]

def solution(numbers, hand):
    answer = ''

    pre_left_hand=[0,3]
    pre_right_hand=[2,3]

    for i in numbers:
        if i in keypad[0]:
            answer+='L'
            pre_left_hand=[0, keypad[0].index(i)]

        elif i in keypad[2]:
            answer+='R'
            pre_right_hand=[2, keypad[2].index(i)]
        
        else:
            l=(1-pre_left_hand[0]) + abs(keypad[1].index(i)-pre_left_hand[1])
            r=(pre_right_hand[0]-1) + abs(keypad[1].index(i)-pre_right_hand[1])

            if r==l:
                if hand=='left':
                    answer+='L'
                    pre_left_hand=[1,keypad[1].index(i)]
                else:
                    answer+='R'
                    pre_right_hand=[1,keypad[1].index(i)]
            elif r>l:
                answer+='L'
                pre_left_hand=[1,keypad[1].index(i)]
            else:
                answer+='R'
                pre_right_hand=[1,keypad[1].index(i)]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))