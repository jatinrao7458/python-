s,k = input().split()
newk= int(k)
FINAL = 0
for i in range (len(s)):
    # line 6 tells that splice the string like the syntax is" name of string [0:to till the number of digit we want in as a number]"
    curr_sum=int(s[i:i+newk])
    if curr_sum > FINAL:
        FINAL= curr_sum
print (FINAL)
    


    

