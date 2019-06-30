import math




def factorize(n):
    count = 2
    i = 2 
    while ( i < n ** 0.5):
        if ( n % i == 0 ):
            count += 2
            # why adding count by 2?
            #because you are conting only until sqrt(n). For eg: if you are trying to find all divisors for 36 -
            #  you will count from 2 to 6. You know that 1&36,2&18, 3&12, 4&9, 6,6 are all divisors and they come in pairs.
        i+= 1

    if ( i ** 2 == n ):
        count += 1
    return count


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
    if ( factorize(triangle) >= 500):
        print(triangle)
        break
    i +=1
