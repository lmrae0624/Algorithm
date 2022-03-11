#divmod: 몫과 나머지를 tuple로 반환

# 10진법을 n진법으로
tmp = '' 
while n > 0:
        n, mod = divmod(n, 3)
        tmp += str(mod)


# n진수를 base진법으로 변환하는것 (중요!)
def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

print(convert(15,16))