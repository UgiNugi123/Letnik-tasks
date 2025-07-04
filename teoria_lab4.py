import math
import heapq

# 1
p = [0.1, 0.2, 0.3, 0.4]
print(-sum(x * math.log2(x) for x in p))

# 2
print(10 * math.log2(8))

# 3
p = [0.5, 0.3, 0.2]
print(sum(-x * math.log2(x) for x in p))

# 4
print(2.0 - 1.8)

# 5
q = {'0': 0.9, '1': 0.1}
h = [[v, k] for k, v in q.items()]
heapq.heapify(h)
while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    for i in range(1, len(a)): a[i] = '0' + a[i]
    for i in range(1, len(b)): b[i] = '1' + b[i]
    heapq.heappush(h, [a[0]+b[0]] + a[1:] + b[1:])
d = dict(h[0][1:])
print(sum(q[k] * len(d[k]) for k in q))

# 6
print(math.log2(16))

# 7
print(math.log2(5))

# 8
print(8 * (1 - 0.1))

# 9
q = {'A': 0.4, 'B': 0.3, 'C': 0.2, 'D': 0.1}
h = [[v, k] for k, v in q.items()]
heapq.heapify(h)
while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    for i in range(1, len(a)): a[i] = '0' + a[i]
    for i in range(1, len(b)): b[i] = '1' + b[i]
    heapq.heappush(h, [a[0]+b[0]] + a[1:] + b[1:])
d = dict(h[0][1:])
print(sum(q[k] * len(d[k]) for k in q))

# 10
a = -0.5 * math.log2(0.5) - 0.5 * math.log2(0.5)
b = -0.9 * math.log2(0.9) - 0.1 * math.log2(0.1)
print(a, b)

# 11
print(100 * 2.5)

# 12
print(-0.75 * math.log2(0.75) - 0.25 * math.log2(0.25))

# 13
print(-1 * math.log2(1))

# 14
q = {'A': 0.5, 'B': 0.3, 'C': 0.2}
h = [[v, k] for k, v in q.items()]
heapq.heapify(h)
while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    for i in range(1, len(a)): a[i] = '0' + a[i]
    for i in range(1, len(b)): b[i] = '1' + b[i]
    heapq.heappush(h, [a[0]+b[0]] + a[1:] + b[1:])
print(dict(h[0][1:]))

# 15
e = 0.1
print(1 + e * math.log2(e) + (1 - e) * math.log2(1 - e))

# 16
a = -0.5 * math.log2(0.5) - 0.5 * math.log2(0.5)
b = -0.9 * math.log2(0.9) - 0.1 * math.log2(0.1)
print(a, b)

# 17
print(2 ** (4 * 5))

# 18
p = [0.4, 0.3, 0.2, 0.1]
print(sum(-x * math.log2(x) for x in p))

# 19
print(2 * 10 * 2)

# 20
p = [0.5, 0.5]
print(-sum(x * math.log2(x) for x in p))
