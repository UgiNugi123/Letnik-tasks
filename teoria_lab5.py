# 1
def (seq):
    prev = None
    return ['-'] + [int(prev == bit) if prev is not None else '-' for prev, bit in zip([None]+seq, seq)]

# 2
def (seq):
    output, prev = [], None
    for bit in seq:
        if bit != prev:
            output.append(bit)
        prev = bit
    return output

# 3
def (seq):
    output, state = [], 0
    for bit in seq:
        if state == 0 and bit == 1: state = 1
        elif state == 1 and bit == 0: state = 2
        elif state == 2 and bit == 1: state = 3
        else: state = 1 if bit == 1 else 0
        output.append(1 if state == 3 else 0)
    return output

# 4
def (seq):
    count = 0
    return [1 if (count := count + bit) % 3 == 0 else 0 for bit in seq]

# 5
def (seq):
    if not seq: return []
    prev, output = seq[0], [1]
    for bit in seq[1:]:
        output.append(1 if bit != prev else 0)
        prev = bit
    return output

# 6
def (seq):
    prev = None
    return ['-'] + [1 if prev == 'a' and c == 'b' else 0 for prev, c in zip([None]+seq, seq)]

# 7
def (seq):
    last, output = [], []
    for bit in seq:
        last.append(bit)
        if len(last) > 3: last.pop(0)
        output.append(1 if len(last)==3 and sum(last)%2==0 else 0)
    return output

# 8
def (seq):
    prev = None
    return ['-'] + [1 if prev == bit else 0 for prev, bit in zip([None]+seq, seq)]

# 9
def (seq):
    parity, output = 0, []
    for bit in seq:
        if bit == 1: parity ^= 1
        output.append(parity)
    return output

# 10
def (seq):
    output, state = [], 0
    for bit in seq:
        if state == 0 and bit == 1: state = 1
        elif state == 1 and bit == 1: state = 2
        elif state == 2 and bit == 0: state = 3
        elif state == 3 and bit == 1: state = 4
        else: state = 1 if bit == 1 else 0
        output.append(1 if state == 4 else 0)
        if state == 4: state = 0
    return output