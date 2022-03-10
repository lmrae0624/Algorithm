# s=[]
# for i in input():
#     s.append(int(i))

# num=len(s)//2
# if sum(s[:num]) == sum(s[num:]):
#     print('LUCKY')
# else:
#     print('READY')


n=input()

result=0
for i in range(len(n)//2):
    result+=int(n[i])

for i in range(len(n)//2,len(n)):
    result-=int(n[i])

if result==0:
    print('LUCKY')
else:
    print('READY')
    
# 5577

# 123402