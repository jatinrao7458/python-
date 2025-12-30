n = list(map(int,input().split()))
# video approch
count=0
final=0
for j in range (len(n)):
    for i in range (1,int(n[j]**1/2)):
        if n[i]%i==0:
            count+=1
        if n[i]*1/2 != i:
            count+=1
        if (count==2):
            final+=1
print(final)





# my approch
intial=0
for i in range (len(n)):
    dummy=0
    for j in range(1,n[i]):
        if n[i]%j==0:
            dummy+=1
        if dummy==2:
                intial+=1
print(intial)