# def solution(A, B):
#     # write your code in Python 3.6
#     A,B = str(A),str(B)
#     lenA,lenB = len(A),len(B)

#     answer=-1
#     for i in range(lenB-lenA+1):
#         if B[i:i+lenA]==A:
#             return i
    
#     return answer

def solution(A, B):
    return str(B).find(str(A))

print(solution(53,1953786))
print(solution(92,10915578653))