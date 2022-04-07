def solution(key, lock):
    m=len(key)
    n=len(lock)

    new_lock=[[0]*(n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    
    def rotate_a_matrix_by_90_degree(a):
        n = len(a) # 행 길이 계산
        m = len(a[0]) # 열 길이 계산
        result = [[0] * n for _ in range(m)] # 결과 리스트
        for i in range(n):
            for j in range(m):
                result[j][n - i - 1] = a[i][j]
        return result

    def check(new_lock):
        for i in range(n,2*n):
            for j in range(n,2*n):
                if new_lock[i][j]!=1: # key랑 lock이랑 반대여야하기 때문에 딱 맞으면 값이 1
                    return False
        return True

    for i in range(2*n):
        for j in range(2*n):
            for _ in range(4):
                key=rotate_a_matrix_by_90_degree(key)
                
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y]+=key[x][y]

                if check(new_lock):
                    return True
                
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y]-=key[x][y]

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))