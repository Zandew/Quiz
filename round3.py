import random, math

'''
  |\
  |b\
  |  \ 
  |   \ C
A |    \
  |     \
  |      \
  |_      \
  |_|_____a\
     B
'''

def r3():
    var = ['A', 'B', 'C', 'a', 'b']
    val1 = random.randint(10, 100)
    var1 = var[random.randint(0,2)]
    solveForSide = random.randint(0, 1)==0
    val2 = None
    var2 = None
    unknown = None
    if (solveForSide):
        var2 = var[random.randint(3, 4)]
        val2 = random.randint(1, 89)
        unknown = var[random.randint(0, 2)]
        while (unknown == var1):
            unknown = var[random.randint(0, 2)]
    else:
        var2 = var[random.randint(0, 2)]
        while (var2 == var1):
            var2 = var[random.randint(0, 2)]
        if (var2 == 'C'):
            val2 = random.randint(val1+1, 100)
        elif (var1 == 'C'):
            val2 = random.randint(10, val1-1)
        else:
            val2 = random.randint(10, 100)
        unknown = var[random.randint(3, 4)]
    print("Given: \n"+str(var1)+" = "+str(val1)+" units\n"+str(var2)+" = "+str(val2)+(" degrees" if solveForSide else " units"))
    print("Solve for "+str(unknown))
    userAns = int(input("Enter your answer rounded to the nearest integer: "))
    ans = None
    if (solveForSide):
        val2 = math.radians(val2)
        if (var1 == 'A'):
            if (var2 == 'a'):
                if (unknown == 'B'):
                    ans = round(val1/math.tan(val2))
                else:
                    ans = round(val1/math.sin(val2))
            else:
                if (unknown == 'B'):
                    ans = round(val1*math.tan(val2))
                else:
                    ans = round(val1/math.cos(val2))
        elif (var1 == 'B'):
            if (var2 == 'a'):
                if (unknown == 'A'):
                    ans = round(val1*math.tan(val2))
                else:
                    ans = round(val1/math.cos(val2))
            else:
                if (var2 == 'b'):
                    if (unknown == 'A'):
                        ans = round(val1/math.tan(val2))
                    else:
                        ans = round(val1/math.sin(val2))
        else:
            if (var2 == 'a'):
                if (unknown == 'A'):
                    ans = round(val1*math.sin(val2))
                else:
                    ans = round(val1*math.cos(val2))
            else:
                if (unknown == 'A'):
                    ans = round(val1*math.cos(val2))
                else:
                    ans = round(val1*math.sin(val2))
    else:
        if (var1 in 'AB' and var2 in 'AB'):
            A = val1 if (var1 == 'A') else val2
            B = val2 if (var1 == 'A') else val1
            if (unknown == 'a'):
                ans = round(math.degrees(math.atan(A/B)))
            else:
                ans = round(math.degrees(math.atan(B/A)))
        elif (var1 in 'BC' and var2 in 'BC'):
            B = val1 if (var1 == 'B') else val2
            C = val2 if (var1 == 'B') else val1
            if (unknown == 'a'):
                ans = round(math.degrees(math.acos(B/C)))
            else:
                ans = round(math.degrees(math.asin(B/C)))
        else:
            A = val1 if (var1 == 'A') else val2
            C = val2 if (var1 == 'A') else val1
            if (unknown == 'a'):
                ans = round(math.degrees(math.asin(A/C)))
            else:
                ans = round(math.degrees(math.acos(A/C)))
    return userAns == ans
print(r3())
