A = int(input())
count = 0
while A>=0:
    if(A%5 == 0):
        count += A//5
        print(count)
        break
    A -= 3
    count += 1
else:
    print(-1)
