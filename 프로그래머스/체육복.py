
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    answer = n-len(lost)

    tmp=[]
    for l in lost:
        if l in reserve:
            answer+=1
            reserve.remove(l)
        else:
            tmp.append(l)
 
    for l in tmp:
        if l-1 in reserve:
            answer+=1
            reserve.remove(l-1)
        elif l+1 in reserve:
            answer+=1
            reserve.remove(l+1)
    return answer


print(solution(5,[2, 4],[1, 4, 5]))


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)