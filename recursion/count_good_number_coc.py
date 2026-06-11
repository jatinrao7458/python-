MOD = 10**9 + 7
def power(x,n ,mod):
    if n==0:
        return 1
    half = power(x, n//2, mod)
    result = (half* half )%mod
    if n % 2 ==1:
        result = (result*x)%mod
    return result
         

def count_good_number(n):
    even_count = (n+1)//2
    odd_count = n//2
    return ((pow(5,even_count,MOD))* (pow(4,odd_count,MOD))) %MOD
result = count_good_number(4)
print(result)