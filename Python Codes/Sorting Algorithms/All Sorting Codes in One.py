# -------------------
# Insertion Sort
# -------------------
def sort(L):
    if L == []:  # Wenn die Leere Liste übergeben wird, dann wird diese zurück gegeben
        return []
    x, R = L[0], L[1:]  # L wird aufgeteilt in das erste Element x und die Restliste R
    return insert(x, sort(R))  # rekursiver Aufruf von insert mit x und R


def insert(x, L):  # L = Die Restliste von der Ursprungsliste!!!
    if L == []:
        return [x]  # Wenn diese Liste 'L' leer ist, dann bestand L nur aus einem Element x und dieses wird zurück gegeben
    y, R = L[0], L[1:]  # Die Restliste wird noch eine Mal aufgeteilt in erstes Elenent y und Rest R
    if x <= y:  # Wenn x <= y ist, dann wird x vor L eingefügt
        return [x] + L
    else:  # An Sonsten muss man Rekursiv insert aufrufen für x und R
        return [y] + insert(x, R)


# -------------------
# Selection Sort
# -------------------

def sort(L):
    if L == []:  # Wenn die leere Liste sortiert werden soll, dann wird diese einfach zurück gegeben
        return []
    x = min(L)  # An Sonsten wird das Minimum aus der List genommen
    return [x] + sort(delete(x, L))  # Das Minimum wird aus der Liste gelöscht und vor die Restliste gesetzt


def delete(x, L):
    if L == []:
        assert L != [], f'delete({x}, [])'
    if L[0] == x:
        return L[1:]
    return [L[0]] + delete(x, L[1:])


# -------------------
# Merge Sort
# -------------------

def sort(L):
    n = len(L)
    if n < 2:  # wenn die Liste aus einem oder keinem Element besteht, dann wird diese so zurück gegeben
        return L
    L1, L2 = L[:n // 2], L[n // 2:]  # Sonst wird die Liste in zwei gleich große Teillisten aufgeteilt
    return merge(sort(L1),
                 sort(L2))  # rekursiver Aufruf von Merge mit beiden Teillisten, welche wieder sortiert werden.


def merge(L1, L2):
    if L1 == []:  # Ist die eine Liste leer, dann wird die andere zurück gegeben
        return L2
    if L2 == []:
        return L1
    x1, R1 = L1[0], L1[1:]  # An Sonsten werden beide Listen aufgeteilt in Anfangselement und Restliste
    x2, R2 = L2[0], L2[1:]
    if x1 <= x2:  # Wenn das erste Element x1 von der ersten liste kleiner ist als erste der zweiten x2, dann
        return [x1] + merge(R1, L2)  # wird x1 zu der gemergten Liste von R1 und L2 hinzugefügt.
    else:
        return [x2] + merge(L1, R2)  # Sonst x2 vor merge(L1,R2)


# -------------------
# Quick Sort
# -------------------

def sort(L):
    if L == []:  # Wenn die leere Liste sortiert werden soll, dann wird diese einfach zurück gegeben
        return L
    x, R = L[0], L[1:]  # L wird aufgeteilt in das erste Element x und die Restliste R
    S = [y for y in R if y <= x]  # Alle Elemente kleiner als x kommen in die Liste S
    B = [y for y in R if y > x]  # Alle Elemente größer als x kommen in die Liste B

    return sort(S) + [x] + sort(B)  # Liste S, das Element x und die Liste B werden zusammen geführt


# -------------------
# Counting Sort
# -------------------

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


# -------------------
# Counting Sort
# -------------------

def extractByte(n, k):
    return n >> (8 * (k - 1)) & 255


def radixSort(L):
    for k in range(1, 4 + 1):
        Grades = [extractByte(n, k) for n in L]
        L = countingSort(L, Grades)[0]

    return L


# ---------------------------
# Heap Sort (Schlechte Wahl)
# ---------------------------

def HeapSort(L):
    H = Nil()
    for p in L:
        H = H.insert(p, None)
        S = []
        while isinstance(H, None):
            p, _ = H.top()
            S.append(p)
            H = H.remove()
        return S


# -------------------------
# Heap Sort (Bessere Wahl)
# -------------------------

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def sink(A, k, n):
    while 2 * k * 1 <= n:
        j = 2 * k + 1
        if j + 1 <= n and A[j] > A[j + 1]:
            j += 1
        if A[k] < A[j]:
            return
        swap(A, k, j)
        k = j


def heap_sort(A):
    n = len(A) - 1
    for k in range((n + 1) // 2 - 1, -1, -1):
        sink(A, k, n)
    while n >= 1:
        swap(A, 0, n)
        n -= 1
        sink(A, 0, n)
