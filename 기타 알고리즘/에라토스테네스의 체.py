import math

n=1000
array=[True]*(n+1)

for i in range(2,int(math.sqrt(n))+1):
    if array[i]:
        j=2 #본인을 제외한 배수를 확인하기 위해서
        while i*j<=n:
            array[i*j]=False
            j+=1
            

for i in range(2,n+1):
    if array[i]:
        print(i,end=' ')
        