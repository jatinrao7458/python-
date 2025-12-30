# Add all its digits until the result has only one digit

# Method 1
n = int(input("enter a number: "))
if n<10:
    print(n)
else:
    # by doing so we can always get the last number jo bilkul last mme milega
    print(n%9)

# method 2
n = (input())
n_int=int(n)
total=0
for i in range (len(n)):
    new=int(n[i])
    total+=new
if n_int<10:
    print(total)
final_str=str(total)
final=0
if n_int>=10:
    for j in range(len(final_str)):
        again=int(final_str[j])
        final+=again
    print(final)

