

def nextNum(n):
    if ( n % 2 == 0):
        return int(n/2)
    else:
        return (3*n) + 1


maxListSize = 0
memories = {}

max_size = 0
max_ele = 0
for element in range (2,9999999):

    size = 0
    given = element
    while (given != 1):
        if ( given not in memories):
            given = nextNum(given)
            size += 1
        else:
            size += memories[given]
            break
        
    memories[element] = size
    if size > max_size:
        max_size = size
        max_ele = element
        
print ( max_ele)
