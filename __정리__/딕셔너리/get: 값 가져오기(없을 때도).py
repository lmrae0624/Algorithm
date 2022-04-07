# dict.get(key,대체 값) : 해당 key가 존재하면 key의 value를 가져오고, 존재하지 않으면 대체값을 가져온다

a={'x':1, "y":2}
print(a.get('x',0))
#1
print(a.get('z',0))
#0
