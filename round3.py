import random

def r3():
    var = ['A', 'B', 'C', 'a', 'b']
    side1 = random.randint(10, 100)
    var1 = var[random.randint(0,2)]
    solveForSide = random.randint(0, 1)==0
    extra = None
    var2 = None
    unknown = None
    if (solveForSide):
        var2 = var[random.randint(3, 4)]
        extra = random.randint(1, 89)
        unknown = var[random.randint(0, 2)]
        while (unknown == var1):
            unknown = var[random.randint(0, 2)]
    else:
        var2 = var[random.randint(0, 2)]
        while (var2 == var1):
            var2 = var[random.randint(0, 2)]
        if (var2 == 'C'):
            extra = random.randint(side1+1, 100)
        elif (var1 == 'C'):
            extra = random.randint(10, side1-1)
        else:
            extra = random.randint(10, 100)
        unknown = var[random.randint(3, 4)]
    print("Given: \n"+str(var1)+" = "+str(side1)+" units\n"+str(var2)+" = "+str(extra)+(" degrees" if not solveForSide else " units"))
    print("Solve for "+str(unknown))
r3()
