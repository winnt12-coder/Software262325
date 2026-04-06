n = int(input())
menu = {}
for i in range(n):
    a, b = input().split()
    if (b == 'enter'):
        menu.update({a: b})
    elif (b == 'leave'):
        del menu[a]
for key in sorted(menu.keys(), reverse=True):
    print(key)
