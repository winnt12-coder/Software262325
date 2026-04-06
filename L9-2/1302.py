N = int(input())
book = []
count = 0
menu = {}

for i in range(N):
    book.append(input())
b = sorted(book)
for ch in b:
    for i in range(N):
        if (ch == b[i]):
            count += 1
        menu.update({ch: count})
    count = 0
m = max(menu, key=menu.get)
print(m)
