n, m=map(int,input().split())
key,lock=[],[]
for _ in range(m):
    key.append(list(map(int,input().split())))
for _ in range(n):
    lock.append(list(map(int,input().split())))


def turn(key):
    new_key=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[i][j]=key[j][m-i-1]

    return new_key


def check(new_lock):
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j]!=1:
                return False
    return True


new_lock=[[0]*(n*3) for _ in range(n*3)]

for i in range(n):
    for j in range(n):
        new_lock[i+n][j+n]=lock[i][j]

result='false'
for i in range(4):
    key=turn(key)

    for x in range(n*2):
        for y in range(n*2):
            for a in range(m):
                for b in range(m):
                    new_lock[x+a][y+b]+=key[a][b]
            
            if check(new_lock):
                result='true'
                break
            else:
                for a in range(m):
                    for b in range(m):
                        new_lock[x+a][y+b]-=key[a][b]
print(result)

# 3 3
# 0 0 0
# 1 0 0 
# 0 1 1
# 1 1 1
# 1 1 0
# 1 0 1