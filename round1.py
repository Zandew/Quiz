'''
Programmed by:  Jason Wei
Programmed on:  January 31, 2019
Programmed for: ICS3U1-04
Purpose:        Create a function which prompts the user once to find the product of a 
                multiplication equation (x*y) or the quotient of a division equation (x/y). 
                The two randomly given numbers (x and y) are guaranteed to be positive integers. Thus,
                the answer must only be a natural number. This function determines the ability of the 
                user to find the answer to a multiplication or division equation. After each question 
                the user will be notified whether they answered the question correctly or not. This
                function will allow the user see an up-to-date score or rules after each
                question if he/she wants to.
'''
# import modules
import random, rules, math

#defining the function
def r1(cor, tot):

    '''
    Parameter: The user's current score and the total number of problems asked so far are
               passed as arguments to dynamically display the score whenever the user
               enters "S" or "s". The user will see their final score at the end.
    Purpose:   This function prompts the user once to find the product of a multiplication
               equation (x*y) or the quotient of a division equation (x/y). The two randomly
               given numbers (x and y) are guaranteed to be positive integers. Thus, the answer must
               only be an natural number. This function determines the ability of the user to find
               the answer to a multiplication or division equation. After each question the
               user will be notified whether they answered the question correctly or not. This
               function will allow the user see an up-to-date score or rules after each
               question if he/she wants to.
    Return:    This function returns True if user answers correctly, and
               False otherwise.
    '''

    
    # randomly generates 0 or 1
    # 0: multiply   1: divide
    md = random.randint(0,1)
    
    # if that number (md) is 1, a division question generates
    if md == 1:
    
        # randomly generates two integers to divide
        x,y = random.randint(2,100),random.randint(2,20)
    
        # if the first number is divisible by the second number,
        # and both numbers are positive,
        # answer will be an natural answer.
        # To generate an answer that is a natural number 
        while x % y != 0:
            x,y = random.randint(2,100),random.randint(2,30)
        
        # prints out the question for the user
        print(x,"/",y,"= ?")
        
        # prompts the answer from the user
        answer = input("Enter your answer: ")
        
        # continues to prompt the user until a valid input is entered
        while answer.isdigit() == False:
            # if the user enters "R" or "r", as stated in rules, rules will be outputed for the user
            if answer == "R" or answer == "r":
                rules.rules()
            # else if the answer is "S" or "s", score will be outputted
            elif answer == "S" or answer == "s":
                print("\n" + "-"*60)
                print("Your current score is",cor,"out of",tot)
                print("You are currently on question #"+str(tot%5+1),"of round #"+str(math.ceil((tot+1)/5)))
                print("-"*60,"\n")
                
            # if the input is not digits only, "r", or "s"
            else:
                print("Your input is invalid! Please try again.\n")
                
            # prints out the question and prompts the user again until the input is digits only
            print(x,"/",y,"= ?")
            answer = input("Enter your answer: ")
            
        # if the answer is correct
        if answer == str(int(x/y)):
            print("Congratulations! You are correct!\n")
            return True
        
        # if the answer is wrong
        else:
            print("You are wrong! The correct answer is",str(int(x/y)) + ".","\n")
            return False
        
    # if that number (md) is 0, a multiplication question generates    
    elif md == 0:
        
        # generates two random numbers from 2 to 20
        x,y = random.randint(2,20),random.randint(2,20)
        
        # prints out the question
        print(x,"x",y,"= ?")
        
        # prompts the user for the answer or intruction (r or s)
        # returns True is answer is right, and False otherwise
        answer = input("Enter your answer: ")
        
        while answer.isdigit() == False:
            
            if answer == "R" or answer == "r":
                rules.rules()
                
            elif answer == "S" or answer == "s":
                print("\n" + "-"*60)
                print("Your current score is",cor,"out of",tot)
                print("You are currently on question #"+str(tot%5+1),"of round #"+str(math.ceil((tot+1)/5)))
                print("-"*60,"\n")
                
            else:
                print("Your input is invalid! Please try again.\n")
                
            print(x,"x",y,"= ?")
            answer = input("Enter your answer: ")
                        
        if answer == str(int(x*y)):
            print("Congratulations! You are correct!\n")
            return True
        
        else:
            print("You are wrong! The correct answer is",str(x*y) + ".","\n")
            return False
