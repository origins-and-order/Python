# source: https://www.youtube.com/watch?v=TYwrHiQ2-G4
from math import log

# for 2^n bits
def hammingcode(stream):

    def build_list(l, count):
        l = l[count-1:]
        t = list()
        while l:
            for i in range(count):
                if l:
                    t.append(l.pop(0))
            for i in range(count):
                if l:
                    l.pop(0)
        return t

    # convert stream to list of bits
    bits = list(stream)

    # calculate exponent
    exponent = int(log(len(bits), 2))

    # find indices for parity bits
    indices = [(2**i)-1 for i in range(exponent+1)]

    # add parity bits
    parity_bits = []

    i = 0
    while len(bits) > exponent-1:
        if i in indices:
            parity_bits.append(None)
        else:
            parity_bits.append(bits.pop(0))
        i+=1

    parity_bits+=bits
    partitions = [build_list(parity_bits, 2**i) for i in range(exponent+1)]

    for index, partition in enumerate(partitions):
        bit_list = []
        for bit in partition:
            if bit:
                bit_list.append(int(bit))
        parity_bits[indices[index]] = sum(bit_list) % 2

    return parity_bits

# s = '01001101'
s = [0,1,0,0,1,1,0,1]
print hammingcode(s) # [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1]
