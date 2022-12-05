PairList = []
with open("In.txt", "r") as data:
    for t in data:
        Line = t.strip()
        A, C = Line.split(",")
        A, B = A.split("-")
        C, D = C.split("-")
        NewTuple = (int(A), int(B), int(C), int(D))
        PairList.append(NewTuple)

Outflanked = 0
Overlap = 0
for p in PairList:
    A, B, C, D = p
    Flanked = False
    if A >= C and B <= D:
        Flanked = True
    elif A <= C and B >= D:
        Flanked = True
    if Flanked:
        Outflanked += 1
    Overlap += 1
    if A > D or B < C:
        Overlap -= 1
    

Part1Answer = Outflanked
Part2Answer = Overlap
        
print(f"{Part1Answer = }")
print(f"{Part2Answer = }")