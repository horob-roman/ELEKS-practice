x1 = int(input("х1: "))
y1 = int(input("у1: "))
x2 = int(input("х2: "))
y2 = int(input("у2: "))

f = x1 * y2 - x2 * y1

if f < 0:
    print("Відрізок OA утворює більший кут з віссю OX")
elif f > 0:
    print("Відрізок OB утворює більший кут з віссю OX")
else:
    print("Відрізки утворюють однаковий кут")
