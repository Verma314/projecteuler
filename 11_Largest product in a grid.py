f = open("numbers.txt")

superList = []

for i in f:
    smallList = []
    smallList += [1,1,1,1]    
    smallList2 = [int(x) for x in i.split(" ")]
    smallList +=(smallList2)
    smallList  += [1,1,1,1]

    superList.append(smallList)
    print(smallList)

for i in range(0,4):
    superList.append([1] * 27)


mulValues = []

print(superList)
for i in range(0,20):
    for j in range(5,23):
        across = 1
        down = 1
        diag = 1
        diag2 = 1
        for k in range(0,4):
            across = across * superList[i][j+k]
            down = down * superList[i+k][j]
            diag = diag * superList[i+k][j+k]
            diag2 = diag2 * superList[i+k][j-k]

        mulValues.append(across)
        mulValues.append(down)
        mulValues.append(diag)
        mulValues.append(diag2)
        
print( max(mulValues)) 
f.close()
