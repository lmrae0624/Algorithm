result={1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0}

# value로 오름차순 후 key만 출력 
sorted(result, key=lambda x : result[x])
sorted(result, key=result.get) #동일
#[3, 4, 2, 1, 5]

# value로 내림차순 후 key만 출력 
sorted(result, key=lambda x : result[x], reverse = True)
sorted(result, key=result.get, reverse = True) #동일
