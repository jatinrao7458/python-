MOD = 10**9+7
def count_good_number(n):
    if n%2 == 0 :
        even_count = int(n/2)
        odd_count_count = int(n/2)
        return (5**even_count)*(4**odd_count_count)

    if n%2 !=0:
        even_count1 = int(n/2)
        odd_count = int(n/2)+1
        return (5**even_count1)*(4**odd_count)
n = 4
result= count_good_number(n)
print(result)