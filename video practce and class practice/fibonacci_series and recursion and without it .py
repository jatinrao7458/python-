# By using recurssion method 
# in this method we need three things :-
# 1.till where we want the fibbonaci series
# 2. first value 
# 3.second digit value 


# return key word helps us to terminate the function
def print_fibonacci(n, a=0, b=1):
    if n < 0:
        return
    if n == 0:
        return
    # line 15 defines the base case
    print(a, end=" ")
    print_fibonacci(n-1, b, a+b)


# Take input from the user: a number
n = int(input(" Enter a number : "))

# Call the print_fibonacci function to print Fibonacci series up to n
print_fibonacci(n)



