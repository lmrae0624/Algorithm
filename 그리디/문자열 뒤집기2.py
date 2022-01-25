s=input()

count=1
tmp=s[0]
for i in range(1, len(s)):
    if tmp!=s[i]:
        count+=1
        tmp=s[i]
        
print(count//2)


    
