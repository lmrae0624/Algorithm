s=input()
length=len(s)//2

result=len(s)
for i in range(1,length+1):
    s_list='' 
    index=0
    count=1
    tmp=s[:index+i]
    
    #for j in range(i, len(s), i): 이렇게도 가능
    while True:
        index+=i
        print(tmp,end=" ")
        if index>len(s):
            s_list+=str(s[index-i:])
            break
        
        if tmp==s[index:index+i]:
            count+=1
        else:
            if count>1:
                s_list+=str(count)
            s_list+=str(tmp)

            count=1
            tmp=s[index:index+i]
    
    print(s_list)
    result=min(result,len(s_list))
print(result)

# aabbaccc
# ababcdcdababcdcd
# abcabcdede
# abcabcabcabcdededededede
# xababcdcdababcdcd