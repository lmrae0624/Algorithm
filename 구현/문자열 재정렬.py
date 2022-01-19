s=input()

alpha=[]
num=[]
for i in s:
    if i.isalpha():
        alpha.append(i)
    else:
        num.append(int(i))
alpha.sort()

if sum(num)>0:
    result=str(sum(num))
else:
    result=''
    
print(''.join(alpha)+result)

# K1KA5CB7