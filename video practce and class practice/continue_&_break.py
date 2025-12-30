# to print number only if its odd
for i in range(1,101,1):
    if i%2 ==0:
        continue
    else:
        print(i);
#  to print number only its is even
for y in range(1,101,1):
    if y%2 ==0:
        print(y);
# other method to print only even 
for z in range (1,21,1):
    if z%2 != 0:
        continue
    else:
        print(z)
# another method to print only prime number
for q in range (1,21, 1):
    if q==1:
        continue
    else:
        print(q)
#  if we want to skipp 7 from printing while printing from 1- 10
for o in range(1,11,1):
    if o==7:
         continue
    else:
        print(o)
# diff betwween break and continue
# Break - terminates the whole loop. It stop the loop over there only
for pp in range (1,21,1):
    if pp ==7:
        break
    else:
        print(pp)

# Continue - Continues the loop by skipping that point
for u in range(1,21,1):
    if u==7:
         continue
    else:
        print(u)
    