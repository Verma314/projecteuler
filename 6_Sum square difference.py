

sum_1 = 0
sum_2 = 0

for i in range(1,101):
    sum_1 +=  i
    sum_2 +=  i * i

print ( sum_1 * sum_1  - sum_2)


#are there other more efficient ways to do it? should I've used the formula?

#updated:
#method 2
n = 100
SUM_2 = int((n * (n+1) * (2*n + 1) ) / 6 )
SUM_1 = (n/2) * (1 + n)
print ( (SUM_1 * SUM_1) - SUM_2)
