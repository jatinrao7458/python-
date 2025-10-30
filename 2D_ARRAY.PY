first =[[1,2,3 ],[4,5,6] , [7,8,9]]
for i in range(len(first)):
    # in nested loopd like this one the j loop will run 9 times and the outer loop will run 3 times 
    for j in range(len(first)):
        print(first[i][j],end = " ")
    print()