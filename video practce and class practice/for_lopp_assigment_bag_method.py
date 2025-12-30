n=int(input("enter a number "))
# using bag method 
#method 1 by sir 
bag=""
for i in range (1,n+1,1):
    bag+=str(i)+",";
print(bag)
# another method 
# method 2
y=int(input("enter a number: "))
bag=""
for i in range (1,y+1,1):
    bag=bag+str(i)+",";
print(bag)
# method 3 
# my method
z=int(input("enter a number:"))
for i in  range(1,z+1,1):
    print(i,end=",");
