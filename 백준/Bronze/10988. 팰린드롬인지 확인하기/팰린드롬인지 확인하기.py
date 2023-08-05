string = input()
for i in range(len(string)):
    if string[i] == string[len(string)-i-1]:
        pd = 1
    else:
        pd = 0
        break
print(pd)