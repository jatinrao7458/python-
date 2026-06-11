# dynamic sliding window
# longest subarray with sum <s here s = 15
# output should be length of longest subarray
arr = [4,5,2,0,1,8,12,3,6,9]
s=15
l,curr,best=-1,0,0
for r in range(len(arr)):
    curr += arr[r]
    while curr> s:
        l +=1
        curr -=arr[l]
    best = max(best,r-l)
print(best)

# fixed sliding window
# maximunm sum of subarray of size k
a=[8,3,-2,4,5,-1,0,5,3,9,-1]
k=5
curr,best=sum(a[:k]),sum(a[:k]) 
for r in range(k,len(a)):
    curr +=a[r] -a[r-k]
    best = max(best,curr)
print(best)
