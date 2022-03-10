def solution(brown, yellow):
    answer = []
    total=brown+yellow

    column=3
    while True:
        if total%column==0:
            row=total//column
            if (row-2)*(column-2)==yellow:
                answer=[row,column]
                break
            else:
                column+=1
        else:
            column+=1

    return answer

print(solution(10,2))
print(solution(24,24))


def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]