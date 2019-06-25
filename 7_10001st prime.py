def sieve(n):
    arr = [0,0] + [1] * n
    for ele_i in range(2, int(len(arr)**0.5)  ):
        if ( arr[ele_i] == 1):
            for ele_j in range( ele_i * ele_i, len(arr) , ele_i):
                arr[ele_j] = 0
    return arr

import math
#how to decide the length of array
# numberOfPrimesUpto(N) ~ N / log (N)
i = 2
while (True):
	if ( i / math.log(i) > 10001):
		print (i)
		break
	i = i + 1
	
arr = sieve (i)

counter = 0
for i in range(0,len(arr)):
    if (arr[i] == 1):
        counter += 1
        if ( counter == 10001):
            print(i)
            


 
