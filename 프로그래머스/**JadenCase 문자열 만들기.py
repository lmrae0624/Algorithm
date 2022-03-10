def solution(s):

    return  " ".join((a[0].upper() + a[1:].lower()) if a!='' else "" for a in s.split(' '))

print(solution("3people  unFollowed me"))
print(solution("for the last week"))
