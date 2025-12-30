# Given a sorted array of integers nums and an integer target, write a program to find the indices of two numbers whose sum equals target. Assume that each input has exactly one solution, and the same element cannot be used twice. If the array is empty or no valid pair is found, print -1. Implement this using the left and right pointer technique.

# Input Format:

# The first line contains an integer representing the size of the array, n.
# The second line contains n space-separated integers, representing the sorted elements of the array nums.
# The third line contains an integer representing the target value.
# Output Format:

# Print two space-separated integers representing the indices of the two numbers that sum to the target.
# If no solution is found or the input array is empty, print -1.

n=list(map(int,input("Enter the array:").split()))
target =int(input("Enter the target :"))
def two_sum(n,target):
    left= 0
    right=len(n)-1
    while left<right:
        s = n[left]+n[right]
        if s==target:
            return [left,right]
        elif s>target:
            right-=1
        else:
            left+=1
result=two_sum(n,target)
print(*result)
