
import math
import heapq

# 1. Энтропия {A:0.5, B:0.3, C:0.2}
p1 = [0.5, 0.3, 0.2]
h1 = -sum(p * math.log2(p) for p in p1)
print(h1)

# 2. Максимальная энтропия для 4 равновероятных исходов
n2 = 4
p2 = [1/n2] * n2
h2 = -sum(p * math.log2(p) for p in p2)
print(h2)

# 3. Энтропия источника {a:0.1, b:0.2, c:0.3, d:0.2, e:0.2}
p3 = [0.1, 0.2, 0.3, 0.2, 0.2]
h3 = -sum(p * math.log2(p) for p in p3)
print(h3)

# 4. Энтропия равна 3 битам при n = 2^3
n4 = 2 ** 3
print(n4)

# 5. Почему энтропия уменьшается?
print("Энтропия уменьшается, когда один символ становится более вероятным, так как неопределённость падает.")

# 6. Хаффман-код {A:0.4, B:0.2, C:0.2, D:0.1, E:0.1}
def huffman_code(probabilities):
    heap = [[weight, [symbol, ""]] for symbol, weight in probabilities.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return dict(sorted(heap[0][1:], key=lambda x: x[0]))

probs6 = {'A': 0.4, 'B': 0.2, 'C': 0.2, 'D': 0.1, 'E': 0.1}
huffman_dict = huffman_code(probs6)
print(huffman_dict)
avg_len6 = sum(probs6[sym] * len(code) for sym, code in huffman_dict.items())
print(avg_len6)

# 7. Почему Хаффман оптимален
print("Код Хаффмана минимизирует среднюю длину кода, он оптимален при известных вероятностях.")

# 8. Арифметический код для 'ABB' при {A:0.6, B:0.4}
def arithmetic_encode(message, probabilities):
    low = 0.0
    high = 1.0
    for symbol in message:
        range_ = high - low
        cum_prob = 0.0
        for s in sorted(probabilities):
            p = probabilities[s]
            if s == symbol:
                high = low + range_ * (cum_prob + p)
                low = low + range_ * cum_prob
                break
            cum_prob += p
    return (low + high) / 2

encoded_val = arithmetic_encode("ABB", {'A': 0.6, 'B': 0.4})
print(encoded_val)

# 9. Декодирование "010100011" с кодами A:0, B:10, C:11
def decode_binary_string(encoded, codebook):
    decoded = ''
    i = 0
    while i < len(encoded):
        for j in range(i + 1, len(encoded) + 1):
            if encoded[i:j] in codebook:
                decoded += codebook[encoded[i:j]]
                i = j - 1
                break
        i += 1
    return decoded

decoded = decode_binary_string("010100011", {'0':'A', '10':'B', '11':'C'})
print(decoded)

# 10. Избыточность
L = 2.5
H = 2.1
redundancy = L - H
print(redundancy)
