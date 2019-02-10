'''
Programmed by:  Albert Chan
Programmed on:  January 31, 2019
Programmed for: ICS3U1-04
Purpose:        Create a function which prompts the user to enter the roots of a
                randomly generated quadratic equation for Round 2 of the Math Quiz.
                All randomly generated quadratic equations will have 2 distinct real
                integer roots. Thus, no randomly generated quadratic equations will
                have no roots, only 1 distinct root, nor any non-integer roots.
'''

# Modules are imported in order to invoke functions from a module
import random, math, rules

'''
Parameter: The user's current score and the total number of problems asked so far are
           passed as arguments to dynamically display the score whenever the
           enters "S" or "s". The user will see their final score at
           the end.
Purpose:   This function prompts the user to enter the roots
           of a randomly quadratic equation (f(x) = ax^2 + bx + c) given,
           after this function is invoked. The random quadratic
           equations given in this function will always have
           2 integer roots. This function determines the ability of the user to
           find the roots of a quadratic equation. After each question the user will be
           notified whether they answered the question correctly or not. This
           function will allow the user see an up-to-date score or rules after each
           question if he/she wants to.
Return:    This function returns True if user answers correctly, but
           False otherwise.
'''

# Round #2 function
def r2(cor, tot):
    
    # Discriminant is originally defined as 0 (explained in next comment)
    d = 0

    '''
    The discriminant of a quadratic equation cannot be less than 0
    (if discriminant is than 0 there are no real roots); in this
    function the discriminant cannot be equal to 0 (if the discriminant
    is 0, there will be only be one distinct real root); this function
    only asks the user to enter the roots of quadratic equations with
    2 distinct real roots
    '''
    while d <= 0:
        
        # The standard form of quadratic equation is f(x) = ax2 + bx + c
        
        # Coefficient a is between -100 and 100 and is randomly generated
        a = random.randint(-100,100)

        '''
        Coefficient a in any quadratic equation cannot be equal to 0,
        thus coefficient a is randomly generated until it is not 0
        '''
        while a == 0:
            a = random.randint(-100,100)

        # Coefficient b is between -100 and 100 and is randomly generated
        b = random.randint(-100,100)

        # Coefficient c is between -100 and 100 and is randomly generated
        c = random.randint(-100,100)

        # Calculation of the discriminant (explanation of what the discriminant can be is explained previously)
        d = (b**2) - (4*a*c)

    # 2 roots of the quadratic equation are calculated
    rt1 = (-b-(math.sqrt(d)))/(2*a)
    rt2 = (-b+(math.sqrt(d)))/(2*a)

    '''
    Determines whether the 2 roots of the quadratic equation are integers; the 2 roots must be integers in this program;
    Coefficients are generated randomly until the 2 roots of the quadratic equation are integers
    '''
    while math.floor(rt1) != math.ceil(rt1) or math.floor(rt2) != math.ceil(rt2):

        # Discriminant is originally defined as 0 (explained in next comment)
        d = 0

        '''
        The discriminant of a quadratic equation cannot be less than 0
        (if discriminant is than 0 there are no real roots); in this
        function the discriminant cannot be equal to 0 (if the discriminant
        is 0, there will be only be one distinct real root); this function
        only asks the user to enter the roots of quadratic equations with
        2 distinct real roots
        '''
        while d <= 0:

            # The standard form of quadratic equation is f(x) = ax2 + bx + c
        
            # Coefficient a is between -100 and 100 and is randomly generated
            a = random.randint(-100,100)

            '''
            Coefficient a in any quadratic equation cannot be equal to 0,
            thus coefficient a is randomly generated until it is not 0
            '''
            while a == 0 :
                a = random.randint(-100,100)

            # Coefficient b is between -100 and 100 and is randomly generated
            b = random.randint(-100,100)

            # Coefficient c is between -100 and 100 and is randomly generated
            c = random.randint(-100,100)

            # Calculation of the discriminant (explanation of what the discriminant can be is explained previously)
            d = (b**2) - (4*a*c)

        # 2 roots of the quadratic equation are calculated
        rt1 = (-b-(math.sqrt(d)))/(2*a)
        rt2 = (-b+(math.sqrt(d)))/(2*a)

    # Formating the output of the quadratic equation to the user based on the values of coefficients (all cases considered)
    print("f(x) = ", end="")
    print(("-" if a<0 else "")+(str(abs(a)) if abs(a)>1 else "")+"x^2 ", end="")
    print(("- " if b<0 else "")+(("+ " if b>0 else "")+str(abs(b)) if abs(b)>1 else "")+("x " if b!=0 else ""), end="")
    print(("- " if c<0 else "")+(("+ " if c>0 else "")+str(abs(c)) if abs(c)>1 else ""))

    # User enters what they believe to be the two roots (separated by a comma) of the quadratic equation that is given (this is not a multiple choice quiz)
    string = input("Enter the 2 roots separated by a comma: ")
    
    # If the string the user enters has 1 comma and the length of the string is greater than 1 (used for error checking)
    if string.count(",") == 1 and len(string) > 1:
        stringSplit0 = string.split(",")[0]
        stringSplit1 = string.split(",")[1]
        splitStrip0 = stringSplit0.strip("-")
        splitStrip1 = stringSplit1.strip("-")
    
    # Checks the input of the user and outputs the corresponding output (error checking and checking the user's input)
    while (string.count(",") != 1 or len(string) == 1 or (string.count(",") == 1 and (not splitStrip0.isdigit() or not splitStrip1.isdigit()))):

        # If the user inputs "R" or "r" the rules of the quiz are outputted to the user
        if (string == "R" or string == "r"):
            rules.rules()

        # If the user inputs "S" or "s" the score of the quiz are outputted to the user
        elif (string == "S" or string == "s"):
            print("\n","-"*60)
            print("Your current score is " + str(cor) + " out of " + str(tot) + ".")
            print("You are currently on question #"+str((tot%5)+1)+" on round #"+str(math.ceil((tot+1)/5)))
            print("-"*60,"\n")

        # If the user inputs an invalid response, the user is prompted to enter what he/she thinks the are 2 roots
        else:
            print("Your input is invalid! Please try again.")

        print()
        
        # Formating the output of the quadratic equation to the user based on the values of coefficients (all cases considered; coefficients determined previously)
        print("f(x) = ", end="")
        print(("-" if a<0 else "")+(str(abs(a)) if abs(a)>1 else "")+"x^2 ", end="")
        print(("- " if b<0 else "")+(("+ " if b>0 else "")+str(abs(b)) if abs(b)>1 else "")+("x " if b!=0 else ""), end="")
        print(("- " if c<0 else "")+(("+ " if c>0 else "")+str(abs(c)) if abs(c)>1 else ""))

        # User inputs their answer
        string = input("Enter the 2 roots separated by a comma: ")

        # If the string the user enters has 1 comma and the length of the string is greater than 1 (used for error checking)
        if string.count(",") == 1 and len(string) > 1:
            stringSplit0 = string.split(",")[0]
            stringSplit1 = string.split(",")[1]
            splitStrip0 = stringSplit0.strip("-")
            splitStrip1 = stringSplit1.strip("-")

    ans1, ans2 = map(int, string.split(","))
    
    # Determining whether the two roots the user enters are correct
    # If the user enters both the correct roots
    if ans1 == rt1 and ans2 == rt2:

        print()
        
        # Outputs if the user enters both the 2 correct roots
        print("Congratulations! You are correct!")

        print()
        
        # Used to determine the score of the user
        return True

    # If the user enters both the correct roots
    elif ans2 == rt1 and ans1 == rt2:

        print()
        
        # Outputs if the user enters both the 2 correct roots
        print("Congratulations! You are correct!")

        print()
        
        # Used to determine the score of the user
        return True

    # If the user enters at least one wrong root
    else:

        print()

        # Outputs if the user enters at least one wrong root
        print("You are wrong!")
        
        # Outputs the 2 correct roots
        print("The 2 correct roots are:", str(int(round(rt1))) + " and " + str(int(round(rt2))))

        print()
        
        # Used to determine the score of the user
        return False
