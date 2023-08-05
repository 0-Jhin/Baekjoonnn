H, M = map(int, input().split())
C = int(input())
M += C
while M >= 60:
    if 60<=M:
        H += 1
        if 24<=H:
            H -= 24
        M -= 60
print(H, M)
