def sort(L):
    if L == []:
        return []
    x, R = L[0], L[1:]
    return insert(x, sort(R))


def insert(x, L):
    if L == []:
        return [x]
    y, R = L[0], L[1:]
    if x <= y:
        return [x] + L
    else:
        return [y] + insert(x, R)


print(sort([9, 7, 8, 0, 5, 6, 4, 1, 2, 3]))


def sort(L):
    if L == []:
        return []
    x = min(L)
    return [x] + sort(delete(x, L))


def delete(x, L):
    if L == []:
        assert L != [], f'delete({x}, [])'
    if L[0] == x:
        return L[1:]
    return [L[0]] + delete(x, L[1:])


print(sort([9, 7, 8, 0, 5, 6, 4, 1, 2, 3]))


def sort(L):
    n = len(L)
    if n < 2:
        return L
    L1, L2 = L[:n // 2], L[n // 2:]
    return merge(sort(L1), sort(L2))


def merge(L1, L2):
    if L1 == []:
       return L2
    if L2 == []:
        return L1
    x1, R1 = L1[0], L1[1:]
    x2, R2 = L2[0], L2[1:]
    if x1 <= x2:
        return [x1] + merge(R1, L2)
    else:
        return [x2] + merge(L1, R2)

print(sort([9, 7, 8, 0, 5, 6, 4, 1, 2, 3]))


def countingSort(Names, Grades):
    assert len(Names) == len(Grades)
    maxGrade = 256
    Counts = [0] * maxGrade
    Indices = [None] * maxGrade
    SortedNames = [None] * len(Names)
    SortedGrades = [None] * len(Names)
    # Phase 1: Counting
    for g in Grades:
        Counts[g] += 1

    # Phase 2: Indexing
    Indices[0] = 0
    for g in range(1, maxGrade):
        Indices[g] = Indices[g - 1] + Counts[g - 1]

    # Phase 3: Distribution
    for i in range(len(Names)):
        grade = Grades[i]
        idx = Indices[grade]
        SortedNames[idx] = Names[i]
        SortedGrades[idx] = Grades[i]
        Indices[grade] += 1
    return SortedNames, SortedGrades


from CountingSort import *

def extractByte(n, k):
    return n >> (8 * (k - 1)) & 255


def radixSort(L):
    for k in range(1, 4 + 1):
        Grades = [extractByte(n, k) for n in L]
        L = countingSort(L, Grades)[0]

    return L


print(radixSort([9, 7, 8, 0, 5, 6, 4, 1, 2, 3]))


def HeapSort(L):
    H = Nil()
    for p in L:
        H = H.insert(p. None)
    S = []
    while isinstance(H, None):
        p, _ = H.top()
        S.append(p)
        H = H.remove()
    return S