string = "hello"
rev_string= "" 
for i in range (len(string)):
    # value is being added in the start of each loop
    rev_string= string[i]+rev_string
print (rev_string)
# or run the loop in reverse 