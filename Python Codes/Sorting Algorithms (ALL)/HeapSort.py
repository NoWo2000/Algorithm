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