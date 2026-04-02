T = int(input())

for i in range(T):
    L = list(input())
    sum = 0

    if (L[0] == ')'):
        print("NO")
    else: 
        for ch in L:
            if(ch == '('):
                sum += 1
            else:
                sum -= 1
            if (sum<0):
                break
        if (sum == 0):
            print("YES")
        else:
            print("NO")
