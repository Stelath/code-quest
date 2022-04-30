def toBinary(inp):
    l,m=[],[]
    for i in inp:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    output = ''
    for binary in m:
        output += str(binary)
    return output

def left_rotate(n, d):
 
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d)|(n >> (32 - d))

n_inputs = int(input())

for i in range(n_inputs):
    str_inp = input()
    hash_inp = input()
    binary = toBinary(str_inp)
    for i in range(128 - (len(binary) % 128)):
        binary += '1'
    binary = [binary[i:i+32] for i in range(0, len(binary), 32)]
    A = int('{:032b}'.format(792250721), 2)
    B = int('{:032b}'.format(683117105), 2)
    C = int('{:032b}'.format(1215387974), 2)
    D = int('{:032b}'.format(1767829900), 2)
    for i, M in enumerate(binary):
        S = (B ^ D) & (C | (~B))
        S = int(('{:032b}'.format(A + S))[-33:], 2)
        S = int(('{:032b}'.format(int(M, base=2) + S))[-33:], 2)
        S = left_rotate(S, i % 32)
        A = D
        D = C
        C = B
        B = S
        A = int(('{:032b}'.format(A))[-33:], 2)
        B = int(('{:032b}'.format(B))[-33:], 2)
        C = int(('{:032b}'.format(C))[-33:], 2)
        D = int(('{:032b}'.format(D))[-33:], 2)
    output = format(A, "b") + format(B, "b") + format(C, "b") + format(D, "b")
    output = hex(int(output, 2))
    print(output[2:].upper())