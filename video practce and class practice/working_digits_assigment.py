#  use while loop  
# take n as input as int
# intially take a variable (gg) as 0 and a variable(miniuu) and  varible (maxii) as 999999 and -999999 respectively
# then use a while loop
# first find the last digit by modulo(n%10)
# then store this value in gg
# then use min and max function 
# as miniuu = min(last, miniuu)
# and maxii = max (last,maxii)
# then divide the input by 10 to remove the last digit
# and then this process will continue




# my difff method
ipp = input()

a= int(ipp[0])
b= int(ipp[1])
c= int(ipp[2])
d= int(ipp[3])
add = sum(a,b,c,d)

print("Sum of digits:",add)
if (a>b and a>d and a>c):
    print("Maximum digit:",a)
elif(b>a and b>c and b>d):
    print("Maximum digit:",b)
elif(c>a and c>b and c>d):
    print("Maximum digit:",c)
else:
    print("Maximum digit",d);
if (a<b and a<d and a<c):
    print("Minimum digit:",a)
elif(b<a and b<c and b<d):
    print("Minimum digit:",b)
elif(c<a and c<b and c<d):
    print("Minimum digit:",c)
else:
    print("Minimum digit:",d);

# by for loop
num = input(" ")
if len(num) == 4 and num.isdigit():
    digits = [int(d) for d in num]
    digit_sum = sum(digits)
    max_digit = max(digits)
    min_digit = min(digits)
    
    print("Sum of digits:", digit_sum)
    print("Maximum digit:", max_digit)
    print("Minimum digit:", min_digit)
else:
    print("Please enter a valid 4-digit number.")