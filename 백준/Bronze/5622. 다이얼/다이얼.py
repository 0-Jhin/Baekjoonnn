alpa=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S = input()
N = 0
for i in range(len(S)):
    for x in range(len(alpa)):
        if S[i] in alpa[x]:
            N += x+3
print(N)