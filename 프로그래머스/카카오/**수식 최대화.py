def calculate(cal,a,b):
    a=int(a)
    b=int(b)
    if cal=='+':
        return str(a+b)
    elif cal=='-':
        return str(a-b)
    else:
        return str(a*b)

def solution(expression):
    from itertools import permutations 
    answer = 0
    cal= ['+', '-', '*']

    num_array=[]
    tmp=''
    for i in expression: #num_array에 숫자랑 기호 끊어서 넣기
        if i.isdigit():
            tmp+=i
        else:
            num_array.append(tmp)
            num_array.append(i)
            tmp=''
    num_array.append(tmp)

    for per in permutations(cal): 
        array=num_array.copy() #list1=list2 하면 2의 값이 바뀔 때 1도 바뀌기 때문에 copy()

        for p in per:
            stack=[]
            while array:
                tmp=array.pop(0)
                if tmp==p:
                    stack.append(calculate(p,stack.pop(),array.pop(0)))
                else:
                    stack.append(tmp)
            array=stack

        answer=max(answer,abs(int(array[0])))
     
    return answer

print(solution("100-200*300-500+20"))


def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list)))) #eval: 문자열 수식을 계산해줌
    return max(answer)