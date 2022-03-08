while True:
    U = float(input("U = "))
    I = float(input("I = "))
    R = float(input("R = "))

    s = R*(0.02/U + 0.004/I)
    print(str(s)[:6]+"\n")
