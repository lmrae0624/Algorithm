# n=int(input())
# d=[1]

# num=2
# while True:
#     if len(d)==n:
#         break
#     if num%2==0:
#         d.append(num)
#     elif num%3==0:
#         d.append(num)
#     elif num%5==0:
#         d.append(num)
#     num+=1

# print(d[n-1])

n=int(input())
d=[0]*n
d[0]=1

i2,i3,i5=0,0,0
x2,x3,x5=2,3,5

for i in range(1,n):
    d[i]=min(x2,x3,x5)
    
    if d[i]==x2:
        i2+=1
        x2=d[i2]*2
    if d[i]==x3:
        i3+=1
        x3=d[i3]*3
    if d[i]==x5:
        i5+=1
        x5=d[i5]*5

print(d[n-1])

