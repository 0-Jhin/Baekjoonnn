A = input()
B=[]
for i in range(97,123):
    if chr(i) in A:
        B.append(A.index(chr(i)))
    else:
        B.append(-1)
print(*B)