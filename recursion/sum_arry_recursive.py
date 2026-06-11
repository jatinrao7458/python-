def sumArrya(arr):
    if arr ==[]:
        return 0
    return arr[0]+sumArrya(arr[1:])
    
sum = sumArrya([1,2,3,4,5])
print(sum)