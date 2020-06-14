unsortierteListeInsert = [2,3,1,4,6,7,9,8,0]
print(f'Before\t\t\t\t\t {unsortierteListeInsert}')

def sort(L): #insertion Sort
    if L == []:
        return []
    x, R = L[0], L[1:]
    return insert(x, sort(R))

def insert(x, L):
    if L == []:
        return [x]
    y, R = L[0], L[1:]
    if x <= y:
        return [x] + [y] + R
    else:
        return [y] + insert(x, R)


print(f'After Insertion Sort\t {sort(unsortierteListeInsert)}')

unsortierteListeSelect = [2,3,1,4,6,7,9,8,0]
#your Code here:
def sort(L):
    if L == []:
        return []
    x = min(L)
    return [x] + sort(delete(x, L))

def delete(x, L):
    if L == []:
        return []
    if L[0] == x:
        return L[1:]
    return [L[0]] + delete(x, L[1:])
print(f'After Selection Sort\t {sort(unsortierteListeSelect)}')

unsortierteListeMerge = [2,3,1,4,6,7,9,8,0]
#your Code here:
def sort(L):
    n = len(L)
    if n < 2:
        return L
    else:
        return merge(sort(L[:n//2]), sort(L[n//2:]))

def merge(L1, L2):
    if L1 == []:
        return L2
    if L2 == []:
        return L1
    x1, R1 = L1[0], L1[1:]
    x2, R2 = L2[0], L2[1:]
    if x1 < x2:
        return [x1] + merge(R1, L2)
    else:
        return [x2] + merge(L1, R2)

print(f'After Merge Sort\t\t {sort(unsortierteListeMerge)}')

unsortierteListeQuick = [2,3,1,4,6,7,9,8,0]
#your Code here:
def sort(L):
    if L == []:
        return []
    x = L[0]
    S = [y for y in L if y < x]
    B = [y for y in L if y > x]
    return sort(S) + [x] + sort(B)
print(f'After Qucick Sort\t\t {sort(unsortierteListeQuick)}')
