import random, math

def round2():
    d = -1
    while d <= 0:
        a = random.randint(-100,100)
        while a == 0:
            a = random.randint(-100,100)
        b = random.randint(-100,100)
        c = random.randint(-100,100)
        d = (b**2) - (4*a*c)

    rt1 = (-b-(math.sqrt(d)))/(2*a)
    rt2 = (-b+(math.sqrt(d)))/(2*a)

    while math.floor(rt1) != math.ceil(rt1) or math.floor(rt2) != math.ceil(rt2):
            d = -1
            while d <= 0:
                a = random.randint(-100,100)
                while a == 0:
                    a = random.randint(-100, 100)
                b = random.randint(-100,100)
                c = random.randint(-100,100)
                d = (b**2) - (4*a*c)

            rt1 = (-b-(math.sqrt(d)))/(2*a)
            rt2 = (-b+(math.sqrt(d)))/(2*a)

    print(str(a) + "x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x", ("+" if c>=0 else "-"), str(abs(c)), "= 0")

    ans1, ans2 = map(int, input("Enter the roots seperated by a space: ").split())

    if ans1 == rt1 or ans2 == rt2:
        print("You are correct!")
        return True
    elif ans2 == rt1 or ans1 == rt2:
        print("You are correct!")
        return True
    else:
        print("You are wrong!")
        print("The correct roots are:", int(round(rt1)), int(round(rt2)))
        return False

round2()
round2()
round2()
round2()
round2()
