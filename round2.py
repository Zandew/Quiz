# Modules are imported in order to invoke functions from the module
import random, math

'''
Parameter: Not applicable for this function (no parameters)

Purpose:   This function prompts the user to enter the roots
           of a randomly quadratic equation (f(x) = ax^2 + bx + c) given,
           after this function is invoked. The random quadratic
           equations given in this function will always have
           2 integer roots. After each question the user will
           be notified whether they answered the question
           correctly or not. This function will allow the user
           see an up-to-date score after each question.
           
Return:    An up-to-date score after each question the user
           answers.
'''

def round2():
    # Discriminant is originally defined as 0 (explained in next comment)
    d = 0

    '''
    The discriminant of a quadratic equation cannot be less than 0
    (if discriminant is than 0 there are no real roots); in this
    function the discriminant cannot be equal to 0 (if the discriminant
    is 0, there will be only be one real root); this function only asks
    the user to enter the roots of quadratic equations with 2 distinct
    real roots
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
        is 0, there will be only be one real root); this function only asks
        the user to enter the roots of quadratic equations with 2 distinct
        real roots
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
    if a == -1 and b == 1 and c == 1:
        print("f(x) = -x^2 + x + 1")
    elif a == -1 and b == 1 and c == 0:
        print("f(x) = -x^2 + x + 0")
    elif a == -1 and b == 1 and c == -1:
        print("f(x) = -x^2 + x - 1")
    elif a == -1 and b == 0 and c == 1:
        print("f(x) = -x^2 + 1")
    elif a == -1 and b == 0 and c == 0:
        print("f(x) = -x^2")
    elif a == -1 and b == 0 and c == -1:
        print("f(x) = -x^2 - 1")
    elif a == -1 and b == -1 and c == 1:
        print("f(x) = -x^2 - x + 1")
    elif a == -1 and b == -1 and c == 0:
        print("f(x) = -x^2 - x")
    elif a == -1 and b == -1 and c == -1:
        print("f(x) = -x^2 - x - 1")
    elif a == 1 and b == 1 and c == 1:
        print("f(x) = x^2 + x + 1")
    elif a == 1 and b == 1 and c == 0:
        print("f(x) = x^2 + x")
    elif a == 1 and b == 1 and c == -1:
        print("f(x) = x^2 + x - 1")
    elif a == 1 and b == 0 and c == 1:
        print("f(x) = x^2 + 1")
    elif a == 1 and b == 0 and c == 0:
        print("f(x) = x^2")
    elif a == 1 and b == 0 and c == -1:
        print("f(x) = x^2 - 1")
    elif a == 1 and b == -1 and c == 1:
        print("f(x) = x^2 - x + 1")
    elif a == 1 and b == -1 and c == 0:
        print("f(x) = x^2 - x")
    elif a == 1 and b == -1 and c == -1:
        print("f(x) = x^2 - x - 1")
    elif a == -1 and b == 1:
        print("f(x) = -x^2 + x", ("+" if c>=0 else "-"), str(abs(c)))
    elif a == -1 and b == 0:
        print("f(x) = -x^2", ("+" if c>=0 else "-"), str(abs(c)))
    elif a == -1 and b == -1:
        print("f(x) = -x^2 - x", ("+" if c>=0 else "-"), str(abs(c)))
    elif a == -1 and c == 1:
        print("f(x) = -x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x + 1")
    elif a == -1 and c == 0:
        print("f(x) = -x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x + 0")
    elif a == -1 and c == -1:
        print("f(x) = -x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x - 1")
    elif a == 1 and b == 1:
        print("f(x) = x^2 + x", ("+" if c>=0 else "-"), str(abs(c)))
    elif a == 1 and b == 0:
        print("f(x) = x^2", ("+" if c>=0 else "-"), str(abs(c)))
    elif a == 1 and b == -1:
        print("f(x) = x^2 - x", ("+" if c>=0 else "-"), str(abs(c)))
    elif a == 1 and c == 1:
        print("f(x) = x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x + 1")
    elif a == 1 and c == 0:
        print("f(x) = x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x")
    elif a == 1 and c == -1:
        print("f(x) = x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x - 1")
    elif b == 1 and c == 1:
        print("f(x) =", str(a) + "x^2 + x + 1")
    elif b == 1 and c == 0:
        print("f(x) =", str(a) + "x^2 + x")
    elif b == 1 and c == -1:
        print("f(x) =", str(a) + "x^2 + x - 1")
    elif b == 0 and c == 1:
        print("f(x) =", str(a) + "x^2 + 1")
    elif b == 0 and c == 0:
        print("f(x) =", str(a) + "x^2")
    elif b == 0 and c == -1:
        print("f(x) =", str(a) + "x^2 - 1")
    elif b == -1 and c == 1:
        print("f(x) =", str(a) + "x^2 - x + 1")
    elif b == -1 and c == 0:
        print("f(x) =", str(a) + "x^2 - x")
    elif b == -1 and c == -1:
        print("f(x) =", str(a) + "x^2 - x - 1")
    elif c == 1:
        print("f(x) =", str(a) + "x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x + 1")
    elif c == 0:
        print("f(x) =", str(a) + "x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x")
    elif c == -1:
        print("f(x) =", str(a) + "x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x - 1")
    elif b == 1:
        print("f(x) =", str(a) + "x^2 + x", ("+" if c>=0 else "-"), str(abs(c)))
    elif b == 0:
        print("f(x) =", str(a) + "x^2", ("+" if c>=0 else "-"), str(abs(c)))
    elif b == -1:
        print("f(x) =", str(a) + "x^2 - 1", ("+" if c>=0 else "-"), str(abs(c)))
    elif a == 1:
        print("f(x) = x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x", ("+" if c>=0 else "-"), str(abs(c)))
    elif a == -1:
        print("f(x) = -x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x", ("+" if c>=0 else "-"), str(abs(c)))
    else:
        print("f(x) =", str(a) + "x^2", ("+" if b>=0 else "-"), str(abs(b)) + "x", ("+" if c>=0 else "-"), str(abs(c)))

    # User enters what they believe to be the two roots (seperated by a comma) of the quadratic equation that is given
    ans1, ans2 = map(int, input("Enter the roots seperated by a comma: ").split(","))

    # Determining whether the two roots the user enters are correct
    if ans1 == rt1 and ans2 == rt2:
        
        print()
        
        # Outputs if the user enters both the 2 correct roots
        print("Congratulations! You are correct!")
        print(" . . .")
        print(". o o .")
        print(". \_/ .")
        print(" . . .")
        
        # Used to determine the score of the user
        return True
    
    elif ans2 == rt1 and ans1 == rt2:
        
        print()
        
        # Outputs if the user enters both the 2 correct roots
        print("Congratulations! You are correct!")
        print(" . . .")
        print(". o o .")
        print(". \_/ .")
        print(" . . .")
        
        # Used to determine the score of the user
        return True
    
    else:
        
        print()
        
        # Outputs if the user enters at least 1 root that is wrong
        print("You are wrong!")
        print(" . . .")
        print(". 0 0 .")
        print(". --- .")
        print(" . . .")
        
        print()

        # Outputs the correct roots to the user if they got at least 1 root wrong
        print("The correct roots are:", str(int(round(rt1))) + "," + str(int(round(rt2))))

        # Used to determine the score of the user
        return False

# Invoking the function for Round #2 of Math Quiz
for i in range(5):
    round2()
    print()
