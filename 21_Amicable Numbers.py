
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



d = {}
for i in range(1,10001):
    d[i] = divisors(i)


for i in d:
    if ( d[i] in d):
        amicableNumbers.add(i)
        amicableNumbers.add(d[i])

print (sum(amicableNumbers))
