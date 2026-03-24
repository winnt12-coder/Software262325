for i in range(3):
    countz = 0
    counto = 0
    a, b, c, d = input().split()

    if(a == '0') :
        countz += 1
    else:
        counto += 1

    if(b == '0') :
        countz += 1
    else:
        counto += 1

    if(c == '0') :
        countz += 1
    else:
        counto += 1

    if(d == '0') :
        countz += 1
    else:
        counto += 1


    if (countz == 4) and (counto == 0) :
        print("D")
    elif (countz == 3) and (counto == 1):
        print("C")
    elif (countz == 2) and (counto == 2):
        print("B")
    elif (countz == 1) and (counto == 3):
        print("A")
    else:
        print("E")
