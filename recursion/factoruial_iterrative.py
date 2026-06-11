def factorial(n):
    ans = n
    for i in range (1,n):
        ans *= n-i
        # another approch and be be like starting from 1
        # ans= 1
        # for i in range(2,n+1) bcz itnial case i.e one is already provided and it will run till n as last value is excluded
        #     ans *=i
    return ans
num = 5
fact= factorial(num)
print(fact)