val_x = [1] * 21
val_x2 = [1] + [0] * 20

lattice = [val_x] + [val_x2] * 20

for i in range(1,21):
    for j in range(1,21):
        lattice[i][j] = lattice[i][j-1] + lattice[i-1][j]

print ( lattice[20][20] )
