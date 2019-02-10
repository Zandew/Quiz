import random, math, rules

'''
Parameter: Not applicable for this function (no parameters)
Purpose:   This function outputs a diagram of a sample triangle
           to the user.
Return:    Not applicable for this function (does not return anything);
           This function only outputs a diagram of a sample triangle to
           the user.
'''
        
def draw():
    print("  |\ ")
    print("  |◡\ ")
    print("  |b \ ")
    print("  |   \ C ")
    print("A |    \ ")
    print("  |     \ \tNote: Not drawn to scale")
    print("  |      \ ")
    print("  |_     a\ ")
    print("  |_|_____(\ ")
    print("      B\n")

'''
Parameter: The user's current score and the total number of problems asked so far are
           passed as arguments to dynamically display the score whenever the
           enters "S" or "s". The user will see their final score at
           the end.
Purpose:   This function prompts the user to solve one other random variable to a given right
           triangle (a side or an angle). The user will be given two variables (which can be
           two side lengths or one side length and one angle). This function determines the
           ability of the user to do primary trigonometry. After each question the user will be
           notified whether they answered the question correctly or not. This
           function will allow the user see an up-to-date score or rules after each
           question if he/she wants to.
Return:    This function returns True if user answers correctly, but
           False otherwise
'''

def r3(cor, tot):
    
    # List of possible given variables
    var = ['A', 'B', 'C', 'a', 'b']
    
    # One of the givens have to be a side
    val1 = random.randint(11, 99)
    var1 = var[random.randint(0,2)]
    
    # Decides whether the user has to solve for a side or to solve for an edge
    solveForSide = random.randint(0, 1)==0
    
    # Initialize second given variable, second given value, and unknown to None
    val2 = None
    var2 = None
    unknown = None
    if (solveForSide):
        # If user has to solve for a side, the user is given a side and an angle
        var2 = var[random.randint(3, 4)]
        val2 = random.randint(1, 89)
        # Selects a random side that is not the same as the given side
        unknown = var[random.randint(0, 2)]
        while (unknown == var1):
            unknown = var[random.randint(0, 2)]
    else:
        # If user has to solve for an angle, the user is given 2 sides
        var2 = var[random.randint(0, 2)]
        # Selects 2 distinct sides for given variables
        while (var2 == var1):
            var2 = var[random.randint(0, 2)]
        # If one of the given sides is the hypotenuse, it must be the longest side
        if (var2 == 'C'):
            val2 = random.randint(val1+1, 100)
        elif (var1 == 'C'):
            val2 = random.randint(10, val1-1)
        else:
            val2 = random.randint(10, 100)
        unknown = var[random.randint(3, 4)]
        
    # Formats the given variables and the variable the user has to solve for
    draw()
    print("Given: \n"+str(var1)+" = "+str(val1)+" units\n"+str(var2)+" = "+str(val2)+(" degrees" if solveForSide else " units"))
    print("Solve for "+str(unknown)+"\n")
    userAns = input("Enter your answer rounded to the nearest integer: ")
    # Keeps asking for input until user enters valid answer
    while not userAns.isdigit():
        if userAns == "R" or userAns == "r":
             rules.rules()
        elif userAns == "S" or userAns == "s":
            print("Your current score is "+str(cor)+" out of "+str(tot))
            print("You are currently on question #"+str((tot)%5+1)+" on round #"+str(math.ceil((tot+1)/5))+"\n")
        else:
            print("Your input is invaild! Please try again.\n")
        draw()
        print("Given: \n"+str(var1)+" = "+str(val1)+" units\n"+str(var2)+" = "+str(val2)+(" degrees" if solveForSide else " units"))
        print("Solve for "+str(unknown))
        userAns = input("Enter your answer rounded to the nearest integer: ")
    userAns = int(userAns)
    ans = None
    
    # Solves for the unknown
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
                
    # Outputs if user is correct or not
    if (userAns == ans):
        print("You are correct!")
    else:
        print("You are wrong! The correct answer is "+str(ans))
    return userAns == ans
