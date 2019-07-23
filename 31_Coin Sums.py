##alright, we have:
##1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) , £2 (200p).
##
##target sum = 200
##
##set = [1,2,5,10,20,50,100,200]
##
##
##problem we have to choose elements from the set,
##the same element possibly multiple times,
##to ensure that the resuling sum to total upto 200
##
##brute force appraoch:
##1. we take a combination of elements at a time (take 2 elements from set, then 3, then 4)
##and with each combination we try to sum them upto 200. Painstaking.
##
##insight:
##2. all the numbers are literally factos of 200, some factors are missings (ex 25)
##we factor 200, and find out the number of ways it can be done,
##
##
##num_factors(200 ) = num_factors (100) + 1 [ +1 because 200 is a factor]
##
##(how do we use this property to simplify our problem?)
##
##
