N, X = map(int,input().split())
A = list(map(int,input().split()))
B = [A[x] for x in range(N) if A[x]<X]
for i in range(len(B)):
    print(B[i], end = " ")