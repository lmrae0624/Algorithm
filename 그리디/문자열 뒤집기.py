s=input()

count=1
data=s[0]
for i in range(1,len(s)):
    if data!=s[i]:
        count+=1
        data=s[i]
        
print(count//2)