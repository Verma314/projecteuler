def isAbundantNumber(n):
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

    if ( sum(divisorList) > n):
        return True



# from 1 to 28123(all nos. greater than this can be written as sum of 2 abundants


abundantNumbers = []
for i in range ( 3, 28123):
    if isAbundantNumber(i):
        abundantNumbers.append(i)


sumsOfAbundantNumbers = set()
for i in abundantNumbers:
    for j in abundantNumbers:
        if ( i+j <= 28123):
            sumsOfAbundantNumbers.add(i+j)


nonAbundantSumNumberList = set(range(1,28124)) - sumsOfAbundantNumbers
print ( sum(nonAbundantSumNumberList) )
