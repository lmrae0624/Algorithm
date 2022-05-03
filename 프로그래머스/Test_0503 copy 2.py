def solution(S):
    info=list(map(str,S.split('\n')))
    
    newinfo={}
    citycount={}
    for i in info:
        name, city, date=i.split(", ")
        photoname, extension = name.split(".")
        
        citycount[city]=citycount.get(city,0)+1

        newinfo[date+","+city]=extension #같은 위치, 동일 시간에 찍은 사진이 없기 때문에 key값으로 설정, 날짜를 앞으로 해서 정렬하는데에 사용
    
   
    for key,extension in sorted(newinfo.items()):
        date,city = key.split(",")
        print(city)
        newinfo[key]=city+"."+extension
    print(newinfo)
        
    
    
    
    pass


def solution(S):
    info=list(map(str,S.split('\n'))) #엔터에 따라 각 정보 나눠서 새로 저장
    
    cityinfo={} # 도시별로 정보를 저장하기 위한 공간
    for i in info:
        name, city, date=i.split(", ") # 콤마(,)로 사진 이름, 도시 이름, 날짜 분리
        photoname, extension = name.split(".") # 온점(.)으로 사진 이름과 확장자명 분리
        
        if city in cityinfo: # 도시별로 [사진날짜, 확장자명] 저장
            cityinfo[city].append([date, extension])
        else:
            cityinfo[city]=[[date, extension]]
    
    newinfo={} #새로운 사진 이름을 저장하기 위한 공간
    for city in cityinfo:
        count=len(cityinfo[city]) #총 도시의 수

        num=1 # 사진 순서를 메기기 위한 num 
        for i in sorted(cityinfo[city]): #사진 날짜 순서대로 정렬
           date, extension =i[0], i[1] 
           newinfo[city+date]=city+str(num).zfill(len(str(count)))+"."+extension #같은 도시, 같은 시간에 찍은 사진이 없기 때문에 key값으로 설정
           num+=1
    
    answer=""
    for i in info:
        name, city, date=i.split(", ")

        answer+=(newinfo[city+date]+'\n')
       
    return answer

#print(solution('photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'))
print(solution('photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2013-09-05 14:08:15\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'))