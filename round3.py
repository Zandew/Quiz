import random

def r3():
    var = ['A', 'B', 'C', 'a', 'b']
    side1 = random.randint(1, 100)
    var1 = var[random.randint(0,2)]
    solveForSide = random.randint(0, 1)==0
    extra = None
    var2 = None
    unknown = None
    if (solveForSide):
        var2 = var[random.randint(3, 4)]
        unknown = var[random.randint(0, 2)]
        while (unknown == var1):
            unknown = var[random.randint(0, 2)]
    else:
        var2 = var[random.randint(0, 2)]
        while (var2 == var1):
            var2 = var[random.randint(0, 2)]
        unknown = var[random.randint(3, 4)]
    print("Given: \n"+str(var1)+" = "+str(side1)+"\n"+str(var2)+" = "+str(extra))
    print("Solve for "+str(unknown))
r3()
