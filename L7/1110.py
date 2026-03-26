N = int(input())
i = N
count = 0

while True:
    x = i//10
    y = i%10
    z = (x+y)%10
    i = y*10+z
    count += 1
    if (i == N):
        break
print(count)
