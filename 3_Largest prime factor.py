def sieve(n):
    arr = [0,0] + [1] * n
    for ele_i in range(2, int(len(arr)**0.5)  ):
        if ( arr[ele_i] == 1):
            for ele_j in range( ele_i * ele_i, len(arr) , ele_i):
                arr[ele_j] = 0
    return arr

#find all prime numbers until SQRT(600851475143)
ans = sieve (int (600851475143 ** 0.5) + 1)

# parse list from top to down, finding largest prime that divides 600851475143

for primes in range ( len(ans)-1, 0, -1 ):
    if ( ans[primes] == 1 and 600851475143 % primes == 0):
        print ( primes)
        break
