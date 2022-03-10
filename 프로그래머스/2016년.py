def solution(a, b):
    day=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month=[31,29,31,30,31,30,31,31,30,31,30,31]

    total=(sum(month[:a-1])+b)%7-1
    
    return day[total]

print(solution(1,31))