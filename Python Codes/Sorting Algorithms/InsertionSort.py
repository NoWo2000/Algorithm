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


print(sort([9,7,8,0,5,6,4,1,2,3]))