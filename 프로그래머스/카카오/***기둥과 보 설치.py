def solution(n, build_frame):
    answer = []

    def check(answer):
        for x,y,a in answer:
            if a==0:
                if y==0:
                    continue
                elif [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                    continue
                else:
                    return False
            else:
                if [x,y-1,0] in answer:
                    continue
                elif [x+1,y-1,0] in answer:
                    continue
                elif [x-1,y,1] in answer and [x+1,y,1] in answer:
                    continue
                else: 
                    return False
        return True

    for x,y,a,b in build_frame:
        if b==1: #설치
            answer.append([x,y,a])
            if not check(answer):
                answer.remove([x,y,a])
        else: #삭제
            if [x,y,a] in answer:
                answer.remove([x,y,a])
                
                if not check(answer):
                    answer.append([x,y,a])

    answer.sort(key=lambda x: (x[0],x[1],x[2]))
    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))