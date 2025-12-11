# first =[[1,2,3 ],[4,5,6] , [7,8,9]]
r = int(input("Enter the numbers of row:"))
c = int(input("Enter the numbers of column"))
first=[]
for e in range(r):
    w=[]
    for q in range(c):
        arr=int(input("enter new elements for matrix :"))
        w.append(arr)
    first.append(w)
for i in range(len(first)):
    # in nested loopd like this one the j loop will run 9 times and the outer loop will run 3 times 
    for j in range(len(first)):
        print(first[i][j],end = " ")
    print()