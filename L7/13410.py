N, K = map(int, input().split())
nums = []

for i in range(1, K+1):
    x = N*i
    y = 0
    while (x>0):
        y = y*10 + x%10
        x //= 10
    nums += [y]

print(max(nums))
