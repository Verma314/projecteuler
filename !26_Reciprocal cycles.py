#WHAT? The recurring cycle of 1/983 is 982 digits long!?!?!!?!?!?!?!

def divByN(n):
    i = 10
    ans =""
    setOfRems = set()
    setOfRems.add((i,i%n))
    length = 0 
    while True:
        soln = i // n
        ans += str(soln)
        remainder = i % n
        #print ( 'remainder is ', remainder)
        i = remainder * 10
        if ( length == 5000):
            return ans
        length += 1
        #setOfRems.add((soln,i))

def findCycle(n):
    for i in range ( 1, 1000, 100):
        twoCharacters = n[2:1000]
        #print( 'searching for ', twoCharacters )
        firstPos = n.find(twoCharacters) 
        #print ( 'frist position ', firstPos) 
        secondPos = n.find(twoCharacters, firstPos + 1 )
        #print ( 'second position ', secondPos) 
        thirdPos = n.find(twoCharacters,secondPos + 1)
        #print ( 'third position ', thirdPos)
        diff1 = secondPos - firstPos
        diff2 = thirdPos - secondPos
        if ( diff1 == diff2):
            return thirdPos-secondPos
    return -1

maxVal = 0
index = 0
for i in range (3,1000):
    value = findCycle ( divByN( i))
    if (value > maxVal ):
        maxVal = value
        index = i

print (index) # 983
print ( maxVal) # 982

    
