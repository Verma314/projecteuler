
def divisors(n):
    count=2 # accounts for 'n' and '1'
    i=2
    divisorList = []
    while(i**2 < n):
        if(n%i==0):
            divisorList.append(i)
            divisorList.append(int(n/i))
            count += 2
        i+=1
    count+=(1 if i**2==n else 0)

    if (i ** 2 == n):
        divisorList.append(i)
    divisorList.append(1)
    return sum(divisorList)

amicableNumbers = set()

for n in range(1,10001):
    a = divisors(n)
    if ( divisors(a) == n and n != a ):
        amicableNumbers.add(a)
        print ( "divisors( "+ str(n)+" )="+ str(a) + ", divisors ("+ str(a) + ")= " +  str(n) )

print( amicableNumbers)
print ( sum(amicableNumbers) )
