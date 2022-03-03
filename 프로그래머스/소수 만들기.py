from itertools import combinations

nums=list(map(int,input().split(',')))

def is_prime_number(x):
    for i in range(2,int(x**0.5)+1+1): #int(x**0.5)+1
        if x%i==0:
            return False
    return True

array=list(combinations(nums, 3))
answer=0
for a in array:
    num=sum(a)
    
    if is_prime_number(num):
        answer+=1
        
print(answer)

#1,2,3,4