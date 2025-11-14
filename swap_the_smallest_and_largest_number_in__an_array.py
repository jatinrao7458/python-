n = int(input("Enter a number: "))
arr=list(map(int,input("Enter a array: ").split()))
greater=max(arr)
smaller=min(arr)
# greater=-999999
# smaller=99999
# for i in range (len(arr)):
#     if arr[i]>greater:
#         greater=arr[i]
# for j in range(len(arr)):
#     if arr[i]<smaller:
#         smaller=arr[i]

print(greater, smaller)
greater_index=arr.index(greater)
smaller_index=arr.index(smaller)
arr[greater_index],arr[smaller_index]=arr[smaller_index],arr[smaller_index]
# * remove the  square brackets from the array
print(*arr)