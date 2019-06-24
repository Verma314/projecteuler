from math import gcd
a = [20, 19, 18, 17, 16, 15 , 14, 13 , 12 , 11]
lcm = a[0]
for i in a[1:]:
  lcm = int(int(lcm*i)/ int (gcd(lcm, i)))
print (lcm)


# because lcm(a,b) * gcd(a,b) = a * b  [WHY?]
# How does GCD even work?
