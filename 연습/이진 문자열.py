def swap(array,start,end):
    temp = [array[start],array[start+1]]

    for i in range(start+2,end+1):
        array[i-2] = array[i]
    
    array[end-1] = temp[0]
    array[end] = temp[1]

def getNextMS(array,start):
    numZero = 0
    numOne = 0 
    for i in range(start,len(array)):
        print("i=",i)
        if i < start + 2 and array[i] !='1':
            return -1
        if array[i] == '1':
            numOne += 1
        else:
            numZero += 1
        
        if numZero == numOne:
            return i
    return -1

binString = "01011000"
array =list(binString)

def largestMagical():
    global array
    for i in range(len(array)-1):
        if array[i] == '0':
            nextMS = getNextMS(array,i+1)
            if nextMS != -1:
                swap(array,i-1,nextMS)

    print(array)
    return array

largestMagical()