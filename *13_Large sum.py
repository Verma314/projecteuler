f = open("13_numbers.py")
sum_ = 0
for i in f:
    sum_ += int(i)

print(str(sum_)[0:10])
