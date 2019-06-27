def sieve(n):
    arr = [0,0] + [1] * n
    for ele_i in range(2, int(len(arr)**0.5)  ):
        if ( arr[ele_i] == 1):
            for ele_j in range( ele_i * ele_i, len(arr) , ele_i):
                arr[ele_j] = 0
    return arr
	
arr = sieve (2000000)

summation = 0
for i in range(0,len(arr)):
    if (arr[i] == 1):
        summation += i
    if ( i >= 2000000):
        break
print(summation)
            


