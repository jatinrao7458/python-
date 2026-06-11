def sum_iterative(arr):
    total =0
    for i in range(len(arr)):
        total+=arr[i]
    return total
r = sum_iterative([1,2,3,4,5])
print(r)