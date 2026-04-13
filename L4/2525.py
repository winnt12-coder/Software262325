A,B = map(int, input().split())
C =int(input())

total = A*60 + B + C

h = (total//60)%24
m = total%60

print(h, m)
