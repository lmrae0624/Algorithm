n=int(input())
time=[]
pay=[]
for _ in range(n):
    t, p=map(int,input().split())
    time.append(t)
    pay.append(p)

d=[0]*(n+1)
result=0

for day in range(n-1,-1,-1):
    t=time[day]+day 
    if t <= n:
        d[day]=max(pay[day]+d[t],result)
        result=d[day]
    else:
        d[day]=result

print(result)
