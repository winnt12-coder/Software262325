Month = int(input())

Day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

first = 4

print("         {}월" .format(Month))
print(" 일 월 화 수 목 금 토")

for i in range(Month-1):
    first = (Day[i]+first)%7

for j in range(first):
    print("   ", end = "")


for i in range(1, Day[Month-1] + 1):
    print(f"{i:2}", end = " ")
    if (first + i) % 7 == 0:
        print()
