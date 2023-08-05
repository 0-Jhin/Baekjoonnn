import sys
input = sys.stdin.readline
n = int(input())
M = [0]*n
for i in range(n):
    C = int(input())
    Q = C//25
    D = (C%25)//10
    N = ((C%25)%10)//5
    P = ((C%25)%10)%5
    M[i]=[Q,D,N,P]
    
for i in range(n):
    print(*M[i])
