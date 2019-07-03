f = open("nos2.txt")

bigList = []
for i in f:
    bigList.append([int(k) for k in i.split(" ")])


solutionList = []
solutionList.append  ( bigList[0])

for i in range(1,len(bigList)):
    
    newSmolList = []
    for j in range (0, len( bigList[i]) ):
        if ( j == 0 ):
            new_val = bigList[i][0] + solutionList[i-1][0]
        elif ( j == len(bigList[i]) - 1):
            new_val = bigList[i][-1] + solutionList[i-1][-1]
        else:
            new_val_1 =  bigList[i][j] + solutionList[i-1][j-1]
            new_val_2 = bigList[i][j] + solutionList[i-1][j]

            new_val = max(new_val_1, new_val_2)
        newSmolList.append(new_val)
        
    solutionList.append(newSmolList)
    
print(max(solutionList[-1]))

f.close()   
