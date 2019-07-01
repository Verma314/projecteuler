
universalHash = {}
universalChainLengths = {}

for i in range (2999998,2,-1):
    if ( i % 2 == 0):
        val = int(i /2)
        universalHash[i] = val
    else:
        val = int((3*i) + 1)
        universalHash[i] = val


def nextVal(n):
    if ( i % 2 == 0):
        return int(i/2)
    else:
        return int((3*i) + 1)
    

#Longest Collatz sequence

def figureChainLen(n):

    if ( n in universalChainLengths ):
        return universalChainLengths[n]
    else:
        chain_length = 0
        value = n 
        while value > 1:
            value = nextVal(value)
            chain_length += 1
        universalChainLengths[n] = chain_length
        return chain_length

    
longestChainLength = 0
startingNumber = 1000000
for i in range ( 100,2,-1):
    chainLen = figureChainLen(i)
    print ( chainLen)
    if chainLen > longestChainLength:
        longestChainLength = chainLen

print (longestChainLength)
