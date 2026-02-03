initial= list(map(int,input("enter the list ot check: ").split())) 
init2= initial.copy()
init2.reverse()
if init2 == initial :
    print("Palindrome")
else:
    print("Not a palindrome")