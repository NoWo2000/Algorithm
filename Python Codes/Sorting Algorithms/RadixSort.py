from CountingSort import *

def extractByte(n, k):
    return n >> (8 * (k - 1)) & 255


def radixSort(L):
    for k in range(1, 4 + 1):
        Grades = [extractByte(n, k) for n in L]
        L = countingSort(L, Grades)[0]

    return L


print(radixSort([9, 7, 8, 0, 5, 6, 4, 1, 2, 3]))
