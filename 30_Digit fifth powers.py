limit = 250000
#based on the graph
a = 100
solution = 0
while limit > 0:
    num = str(a)

    sum_ = 0
    for i in num:
        #print ( "compute ", i , " ^ 4 = ", int(i) ** 4 )
        sum_ += int(i) ** 5
    #print ( "sum : ", sum_)
    if (sum_ == int(num)):
        solution += int(num)
        #print ( "we're here")
        print ( num)
        
    a += 1
    limit -= 1

print ( 'solution', solution)

#4150 + 4151 +54748 +92727 +93084 +194979
# solution 443839
