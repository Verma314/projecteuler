a = 1
b = 1

index = 3
while True:
    c = a + b

    if ( len (str(c)) == 1000 ):
        print (index)
        break

    a = b
    b = c
    index += 1
