n=int(input())
array=[]
for _ in range(n):
    data=list(map(str,input().split()))
    array.append((data[0],int(data[1]),int(data[2]),int(data[3])))

array=sorted(array, key=lambda x:(-x[1],x[2],-x[3],x[0]))

print('------------------')
for i in range(n):
    print(array[i][0],array[i][1],array[i][2],array[i][3])


# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90