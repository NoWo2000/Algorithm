def sort(L):
    if L == []:
        return L
    x, R = L[0], L[1:]
    S = [y for y in R if y <= x]
    B = [y for y in R if y > x]

    return sort(S) + [x] + sort(B)


print(sort([9, 7, 8, 0, 5, 6, 4, 1, 2, 3]))