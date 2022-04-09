def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        remove = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove[i][j], remove[i][j+1], remove[i+1][j], remove[i+1][j+1] = 1, 1, 1, 1

        count = 0
        for i in range(m):
            count += sum(remove[i])
        
        if count == 0:
            break
        answer += count

        for i in range(m-1, -1, -1): #터진거 내리기 아래서부터 반복문 시작 
            for j in range(n):
                if remove[i][j] == 1:
                    x = i-1 #위에칸 index
                    while x >= 0 and remove[x][j] == 1: #remove가 1이 아닐때까지 위로 올라가기
                        x -= 1
                    if x < 0: 
                        board[i][j] = 0 #제일 윗줄이면 0으로 바꾸기
                    else:
                        board[i][j] = board[x][j] #안터진 값을 아래로 내리고
                        remove[x][j] = 1 #그 위치를 터졌다고 변경
          
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))

