import streamlit as st
def sieve_of_eratosthenes(n):
    is_prime=['True']*(n+1)
    is_prime[0]=is_prime[1]='False'
    i=2
    for i in range(2,n):
        if is_prime[i]=='True':
            for j in range(i*i,n+1,i):# the third argument is for skipping
                is_prime[j]='False'
    for i in range(n+1):
        if(is_prime[i]=='True'):
            return is_prime
st.title("Prime number Finder")
num=st.number_input("Enter the upper limit (num):" ,min_value=2, value=30 , step=1)
if(st.button("Print the prime no's")):
    primes=sieve_of_eratosthenes(num)
    for prime in primes:
        st.text(prime)