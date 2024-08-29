#sieve of eratosthenes
n=30
is_prime=['True']*(n+1)
is_prime[0]=is_prime[1]='False'
i=2
for i in range(2,n):
    if is_prime[i]=='True':
        for j in range(i*i,n+1,i):# the third argument is for skipping
            is_prime[j]='False'
for i in range(n+1):
    if(is_prime[i]=='True'):
       print(i)