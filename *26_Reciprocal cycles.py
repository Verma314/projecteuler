from decimal import *


def divByN(n):
    i = 10
    ans =""
    setOfRems = set()
    setOfRems.add((i,i%n))

    time = dict()
    time_val = 0
    
    
    
    while True:
        soln = i // n
        ans += str(soln)

        time[(i,i%n)] = len(ans) -1 
        time_val += 1
        
        remainder = i % n
        #print ( 'remainder is ', remainder)
        if ( remainder == 0 ):
            return 0
        
        i = remainder * 10

        
        if ( (soln,i) in setOfRems):
            val = time[(soln,i)]
            #print ( ans[ time[(soln,i)]::-1] )
            
            return len(ans)

        setOfRems.add((soln,i))

maxValue = 0
maxIndex = 0
for i in range( 2,50):
     valueLength = divByN(i)
     if ( valueLength > maxValue):
         maxValue = valueLength
         maxIndex = i
print ( i)
