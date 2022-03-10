def calculate(cal,a,b):
    if cal=='+':
        return a+b
    elif cal=='-':
        return a-b
    else:
        return a*b

def solution(expression):
    from itertools import permutations 
    answer = 0
    cal= ['+', '-', '*']

    array=[]
    tmp=''
    for i in expression:
        if i.isdigit():
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=''
    array.append(tmp)


    for per in permutations(cal):
        new_array=array
        for i in per:
            for j in range(len(new_array)):
                if new_array[j]==i:
                    print(j,array[j])
                    print(new_array)
                    new_array[j-1]=calculate(new_array[j],int(new_array[j-1]),int(new_array[j+1]))
                    new_array[j+1]=new_array[j-1]

        print(new_array)  
        for a in new_array:
            print(a)
            if any(b.isdigit() for b in a):
                answer=max(answer,abs(int(a)))  
    print(array)
    return answer

print(solution("100-200*300-500+20"))