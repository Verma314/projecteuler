import math

def factorize(n):
    facs = []
    for i in range(1, int(n/2) + 2):
        if ( n % i == 0 ):
            facs.append(i)
    facs.append(n)
    return len(facs) 

def divisors(n):
    count=2 # accounts for 'n' and '1'
    i=2
    while(i**2 < n):
        if(n%i==0):
            count+=2
        i+=1
    count+=(1 if i**2==n else 0)
    return count

#generate triangle numbers:
i = 1000
while (True):
    triangle = int((i/2) * (1 + i))
    if ( divisors(triangle) >= 500):
        print(triangle)
        break
    i +=1
