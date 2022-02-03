import itertools

l, c=map(int,input().split())
array=list(map(str,input().split()))
array.sort()

vowels = ('a', 'e', 'i', 'o', 'u') 

for password in itertools.combinations(array,l):
    count=0
    for p in password:
        if p in vowels:
            count+=1
        
    if count>=1 and count<=l-2:
        print(''.join(password))

# 4 6            
# a t c i s w