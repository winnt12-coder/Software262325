A,B = map(int, input().split())
if A>B:
    A,B = B,A
total = (B-A+1)*(A+B)//2
print(total)
