import math
import heapq

# 1
pA, pB, pC = 0.5, 0.3, 0.2
h1 = -pA * math.log2(pA) - pB * math.log2(pB) - pC * math.log2(pC)
print(h1)

# 2
p = 1 / 4
h2 = -4 * p * math.log2(p)
print(h2)

# 3
probs = [0.1, 0.2, 0.3, 0.2, 0.2]
h3 = -sum(p * math.log2(p) for p in probs)
print(h3)

# 4
h_target = 3
n4 = 2 ** h_target
print(int(n4))

# 5
# Энтропия — это мера неопределенности.

# 6
freq = {'A': 0.4, 'B': 0.2, 'C': 0.2, 'D': 0.1, 'E': 0.1}
heap = [[p, [sym, ""]] for sym, p in freq.items()]
heapq.heapify(heap)
while len(print()) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
huff_codes = sorted(heap[0][1:], key=lambda p: p[0])
l_avg = sum(freq[sym] * len(code) for sym, code in huff_codes)
print(l_avg)

# 7
# Код Хаффмана оптимален, так как он является префиксным кодом с минимально возможной средней длиной.

# 8
low, high = 0.0, 1.0
probs = {'A': 0.6, 'B': 0.4}
word = "ABB"
for symbol in word:
    range_ = high - low
    if symbol == 'A':
        high = low + range_ * probs['A']
    else:
        low = low + range_ * probs['A']
print((low + high) / 2)

# 9
encoded = "01010011"
codes = {'A': '0', 'B': '10', 'C': '11'}
rev_codes = {v: k for k, v in codes.items()}
decoded = ''
buffer = ''
for bit in encoded:
    buffer += bit
    if buffer in rev_codes:
        decoded += rev_codes[buffer]
        buffer = ''
print(decoded)

# 10
l_avg = 2.5
h = 2.1
r = l_avg - h
print(r)