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
