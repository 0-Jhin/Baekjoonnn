a, b, c = map(int, input().split())
if a != b and b != c and a != c:
    if a > b and a > c:
        print(a*100)
    elif b > a and b > c:
        print(b*100)
    else:
        print(c*100)
elif a==b==c:
    print(a*1000+10000)
else:
    if a == b or a == c:
        print(a*100+1000)
    else:
        print(b*100+1000)
