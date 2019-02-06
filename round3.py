import random, math

'''
  |\
  |◡\
  |b \ 
  |   \ C
A |    \
  |     \
  |      \
  |_     a\
  |_|_____(\
      B
'''

def r3(cor, tot):
    
    #list of possible given variables
    var = ['A', 'B', 'C', 'a', 'b']
    
    #One of the givens have to be a side
    val1 = random.randint(10, 100)
    var1 = var[random.randint(0,2)]
    
    #Decides whether the user has to solve for a side or to solve for an edge
    solveForSide = random.randint(0, 1)==0
    
    #initialize second given variable, second given value, and unknown to None
    val2 = None
    var2 = None
    unknown = None
    if (solveForSide):
        #If user has to solve for a side, the user is given a side and an angle
        var2 = var[random.randint(3, 4)]
        val2 = random.randint(1, 89)
        #selects a random side that is not the same as the given side
        unknown = var[random.randint(0, 2)]
        while (unknown == var1):
            unknown = var[random.randint(0, 2)]
    else:
        #If user has to solve for an angle, the user is given 2 sides
        var2 = var[random.randint(0, 2)]
        #selects 2 distinct sides for given variables
        while (var2 == var1):
            var2 = var[random.randint(0, 2)]
        #if one of the given sides is the hypotenuse, it must be the longest side
        if (var2 == 'C'):
            val2 = random.randint(val1+1, 100)
        elif (var1 == 'C'):
            val2 = random.randint(10, val1-1)
        else:
            val2 = random.randint(10, 100)
        unknown = var[random.randint(3, 4)]
        
    #formats the given variables and the variable the user has to solve for
    print("Given: \n"+str(var1)+" = "+str(val1)+" units\n"+str(var2)+" = "+str(val2)+(" degrees" if solveForSide else " units"))
    print("Solve for "+str(unknown))
    userAns = input("Enter your answer rounded to the nearest integer: ")
    #keeps asking for input until user enters valid answer
    while not userAns.isdigit():
        if userAns == "R" or userAns == "r":
             rules.rules()
        elif userAns == "S" or userAns == "s":
            print("Your current score is "+str(cor)+" out of "+str(tot))
            print("You are currently on question #"+str((tot)%5+1)+" on round #"+str(ceil((tot+1)/5)))
        else:
            print("Your input is invaild! Please try again.")
        print("Given: \n"+str(var1)+" = "+str(val1)+" units\n"+str(var2)+" = "+str(val2)+(" degrees" if solveForSide else " units"))
        print("Solve for "+str(unknown))
        userAns = input("Enter your answer rounded to the nearest integer: ")
    userAns = int(userAns)
    ans = None
    
    #Solves for the unknown
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
                
    #outputs if user is correct or not
    if (userAns == ans):
        print("You are correct!")
    else:
        print("You are wrong! The correct answer is "+str(ans))
    return userAns == ans
