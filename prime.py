i=3
count=0
n=1
print(2)
for i in range(i,10):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
    if(count>=1):
        print('The given number is not a prime no.')
        print(i)
    else:
        print('The given number is a prime no.')
        print(i)
        n+=1
print(f"Total prime number"+str(n))




