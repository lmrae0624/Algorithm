def solution(cacheSize, cities):
    answer = 0

    if cacheSize==0:
        return len(cities)*5

    cache = []
    for c in cities:
        if c.lower() in cache:
            answer+=1
            cache.remove(c.lower())
            cache.insert(len(cities) - 1, c.lower())
        else:
            answer+=5
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(c.lower())

    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))


