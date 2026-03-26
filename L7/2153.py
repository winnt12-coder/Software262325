li = list(input())
total = 0

for i in range(len(li)):
    l = li[i]

    if(97 <= ord(l) <=122):
        total += ord(l)-96
    elif(65 <= ord(l) <= 90):
        total += ord(l)-38

if (total == 1):
    print("It is a prime word.")
else:
    for j in range(2, total):
        if(total%j == 0):
            print("It is not a prime word.")
            break
    else:
        print("It is a prime word.")
