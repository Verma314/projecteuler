

def isPallin (x):
    if ( str(x) == str(x)[::-1]):
        return True
    else:
        return False


listOfPallins = {}
listOfSolns = []
for i in range ( 999,99,-1):
    for j in range ( 990,99,-11): #one of the numbers has to be divisible by 11, do the math
        if ( isPallin(i*j) ):
            listOfSolns.append(i*j)
            listOfPallins[i*j] = str(i) + " * " + str(j) 



    if ( i < 500 and j < 500):
        break

print ( max(listOfSolns) )
