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