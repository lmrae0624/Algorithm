n, k = map(int,input().split())
count=0

while True:
    if n<k:
        break
    count+=n%k+1 
    n//=k

count+=n-1 #n<k일때 반복문 탈출했기 때문에 남은 n에 대해서 더해주기
print(count)