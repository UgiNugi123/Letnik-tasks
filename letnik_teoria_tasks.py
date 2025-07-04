
import math

# 1
n = 10
m = 4
i1 = n * math.log2(m)
print(i1)

# 2
m = 8
i2 = math.log2(m)
print(i2)

# 3
bits = 5
i3 = 2 ** bits
print(i3)

# 4
max_number = 31
i4 = math.ceil(math.log2(max_number + 1))
print(i4)

# 5
p0 = 0.5
p1 = 0.5
h5 = -p0 * math.log2(p0) - p1 * math.log2(p1)
print(h5)

# 6
pA = 0.7
pB = 0.2
pC = 0.1
h6 = -pA * math.log2(pA) - pB * math.log2(pB) - pC * math.log2(pC)
print(h6)

# 7
m = 33
i7 = math.log2(m)
print(i7)

# 8
pA = 0.5
pB = 0.3
pC = 0.2
lA = 1
lB = 2
lC = 3
l_avg = pA * lA + pB * lB + pC * lC
h8 = -pA * math.log2(pA) - pB * math.log2(pB) - pC * math.log2(pC)
print(l_avg, h8)

# 9
n = 6
m = 3
i9 = m ** n
print(i9)

# 10
n = 5
m = 26
i10 = n * math.log2(m)
print(i10)
