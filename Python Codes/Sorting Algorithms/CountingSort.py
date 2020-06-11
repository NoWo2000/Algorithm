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


#Der folgende Code dient nur zur Veranschaulichungszwecken des Algorithmus
Data = [
    ('Alexander', 4),
    ('Benjamin', 2),
    ('Daniel', 3),
    ('David', 3),
    ('Elijah', 2),
    ('Gabriel', 1),
    ('Henry', 2),
    ('Jacob', 5),
    ('James', 3),
    ('Joseph', 2),
    ('Liam', 2),
    ('Logan', 3),
    ('Lucas', 1),
    ('Mason', 2),
    ('Matthew', 5),
    ('Michael', 3),
    ('Noah', 4),
    ('Oliver', 2),
    ('Owen', 4),
    ('Samuel', 3),
    ('Sebastian', 2),
    ('William', 1)
]

pNames = [n for n, _ in Data]
pGrades = [g for _, g in Data]

SortedNames, SortedGrades = countingSort(pNames, pGrades)
SortedData = zip(SortedNames, SortedGrades)

for n, g in SortedData:
        print('%-9s: %1d' % (n, g))
