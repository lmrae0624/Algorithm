str1=[1,2,3,4]
str2=[3,4,5,6]

# 교집합
gyo = set(str1) & set(str2)
print(set(str1).intersection(set(str2)))

# 합집합
hap = set(str1) | set(str2)
print(set(str1).union(set(str2)))
print(gyo,hap)