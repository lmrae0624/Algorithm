#divmod: 몫과 나머지를 tuple로 반환

# 10진법을 n진법으로
tmp = '' 
while n > 0:
        n, mod = divmod(n, 3)
        tmp += str(mod)

# n진법을 10진법으로 변환
print(int('101',2)) 
print(int('202',3))
print(int('303',4))
print(int('404',5))
print(int('505',6))
print(int('ACF',16))

# 10진법을 변환
print(bin(11)) #2진법
print(oct(11)) #8진법
print(hex(11)) #16진법

print(bin(11)[2:])
print(oct(11)[2:])
print(hex(11)[2:])


# 10진법을 n진법으로 바꾸기
def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base) #정수를 나눈 몫과 나머지를 구하는 함수
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

print(convert(15,16))