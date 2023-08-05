n = int(input())
for i in range(1, n+1):
    for x in range(n, i, -1):
        print(" ",end="")
    for y in range(i):
        print("*",end="")
    print("")
