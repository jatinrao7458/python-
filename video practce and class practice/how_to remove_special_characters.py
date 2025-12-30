n = input("Enter a random string ")
# we will make an empty variable to store the later characters
result = ""

# this loop we will run for all the elements in n
for i in  n:
    if(i>="a" and i<="z") or (i>="A" and i<="Z"):
        result+=i
    else:
        continue
print(result)


