# 문자열을 대문자로 변경하는 방법
s1 = 'BlockDMask' 
s2 = s1.upper()
# BLOCKDMASK

# 문자열을 소문자로 변경하는 방법
s1 = 'BlockDMask' 
s2 = s1.lower()
# blockdmask


## 판별
# 문자가 대문자인지 확인하는 방법
s1 = 'BlockDMask' 
s2 = s1.upper()
print('{0} 대문자? : {1}'.format(s1, s1.isupper())) # False 
print('{0} 대문자? : {1}'.format(s2, s2.isupper())) # True

# 문자가 소문자인지 확인하는 방법
s2.islower()

#대문자 
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha='abcdefghijklmnopqrstuvwxyz'