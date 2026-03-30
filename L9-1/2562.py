L = []
for i in range(9):
    L.append(int(input()))
x = max(L)

print(x)
print(L.index(x)+1)
