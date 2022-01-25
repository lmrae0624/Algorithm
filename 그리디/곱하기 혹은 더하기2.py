array=list(map(int,input()))

result=0
for a in array:
    if result<=1 or a<=1:
        result+=a
    else:
        result*=a
print(result)

# 02984
# =567