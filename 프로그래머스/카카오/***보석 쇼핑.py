def solution(gems):
    type=set(gems)

    left,right=0,0
    
    re_left,re_right=0,len(gems)
    while left<=right:
        if type == set(gems[left:right+1]): #슬라이싱에서 효율성 실패....
            if (re_right-re_left) > (right-left):
                re_left,re_right=left,right
            left+=1
        else:
            if right<len(gems):
                right+=1
            else:
                break
                
    return [re_left+1,re_right+1]

# dict로 다시 
def solution(gems):
    type=len(set(gems))

    left,right=0,0
    x,y=0,len(gems)-1
    
    check={gems[right]:1}
    while left<=right and right<len(gems):
        if type == len(check): 
            if (y-x) > (right-left):
                x,y=left,right
            
            if check[gems[left]]==1:
                del check[gems[left]]
            else:
                check[gems[left]]-=1
            left+=1
        else:
            right+=1
            if right<len(gems):
                check[gems[right]]=check.get(gems[right],0)+1
                
    return [x+1,y+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["XYZ", "XYZ", "XYZ"]))