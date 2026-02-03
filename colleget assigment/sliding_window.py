from collections import deque



def slidingwindow(nums, k):
    # we will store the value of index which we will be taking out
    dq= deque()
    # to store the max value 
    result=[]
    for i in range (len(nums)):
        while dq and dq[0] < i-k+1:
            dq.popleft()
        while dq and nums[dq[-1]<nums[i]]:
            dq.pop()
        dq.append(i)
        if i>k-1:
            result.append(nums[dq[0]])
    return result
# size of array
n = int(input())
nums = list(map(int,input().split()))
# k value of silding window
k = int(input())
nums.sort()
ans = slidingwindow(nums,k)
print(*ans)