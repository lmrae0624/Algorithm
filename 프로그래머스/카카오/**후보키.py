
def solution(relation):
    from itertools import combinations
    row=len(relation)
    col=len(relation[0])

    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))

    print(combi)

     #유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        print(tmp)
        if len(set(tmp)) == row:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성 # x가 i의 부분집합인지 확인
                    put = False
                    break

            if put: 
                unique.append(i)
   
    return len(unique)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))