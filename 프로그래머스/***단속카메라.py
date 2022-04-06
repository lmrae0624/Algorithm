def solution(routes):
    answer = 0
    routes.sort(key= lambda x: (x[1])) # 나가는 지점 기준으로 오름차순
    print(routes)

    camera=-30001
    for x,y in routes:
        if x<=camera : # 들어오는거만 확인해도 됨
            continue
        
        camera=y
        answer+=1

    return answer

print(solution([[-20, 15], [-14,-5], [-18,-13], [-5,-3]]))
print(solution([[1,1], [-20,-13], [-18,-13], [-5,-3]]))
