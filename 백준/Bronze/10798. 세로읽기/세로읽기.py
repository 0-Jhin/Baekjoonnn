S = []
x=[]
for i in range(5):
    S.append(input())
    x.append(len(S[i]))

for i in range(max(x)):
    for j in range(5):
        if len(S[j])<=i:
            pass
        else:
            print(S[j][i],end='')
