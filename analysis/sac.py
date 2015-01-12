from math import log
def display(mat):
    """ Return SAC in the understandable form """

    # List of Columns
    p = '\n       '
    for i in range(8):
        p += '%02x' % i + '    '
    p += '\n'

    for i in range(60):
        p += '-'
    p += '\n'

    # Row
    for i in range(8):
        p += '%02x' % i + '  |  '

        # Entries
        for j in mat[i]:
            p +=  str(j) + '   '
        p += '\n'

    return p.upper()
def sac(S):
        """Strict Avalanche Effect
        http://www.cs.rit.edu/~caw4567/docs/caw_thesis_library.pdf
        """
        order = len(S)
        n = int(log(order, 2))
        bitBucket = []
        for i in range(n):
                bucket = []
                for j in range(n):
                        bucket.append(0)
                bit = 1 << i
                for x in range(order):
                        xorDiff = S[x]^S[x^bit]
                        for b in range(n):
                                if (((1 << b) & xorDiff) != 0):
                                        bucket[b] = bucket[b] + 1
                bitBucket.append(bucket)
        print(display(bitBucket))
        return bitBucket
