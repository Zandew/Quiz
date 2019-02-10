import random, rules, math

'''
Parameter: The user's current score and the total number of problems asked so far are
           passed as arguments to dynamically display the score whenever the user
           enters "S" or "s". The user will see their final score at
           the end.
Purpose:   This function prompts the user to find the product of a multiplication
           equation (x*y) or the quotient of a division equation (x/y). The two randomly
           given integers (x and y) are guaranteed to the integers. Thus, the answer must
           only be an integer. This function determines the ability of the user to find
           the answer to a multiplication or division equation. After each question the
           user will be notified whether they answered the question correctly or not. This
           function will allow the user see an up-to-date score or rules after each
           question if he/she wants to.
Return:    This function returns True if user answers correctly, but
           False otherwise.
'''

def r1(cor, tot):
        
    x,y = random.randint(2,100),random.randint(2,20)
    md = random.randint(0,1) #   0: multiply   1: divide
    if md == 1:
        while x % y != 0:
            x,y = random.randint(1,100),random.randint(1,30)
            
        print(x,"/",y,"= ?")
        
        answer = input()
        
        while answer.isdigit() == False:
            if answer == "R" or answer == "r":
                rules.rules()
            elif answer == "S" or answer == "s":
                print("-"*60)
                print("Your current score is",cor,"out of",tot)
                print("You are currently on question #"+str(tot%5+1),"on round #"+str(math.ceil((tot+1)/5)))
                print("-"*60,"\n")
            else:
                print("Your input is invalid! Please try again.")
            print(x,"/",y,"= ?")
            answer = input()
        if answer == str(int(x/y)):
            print("Congratulations! You are correct!\n")
            return True
        else:
            print("You are wrong! The correct answer is",str(int(x/y)) + ".","\n")
            return False
    elif md == 0:
        x,y = random.randint(2,20),random.randint(2,20)
        print(x,"x",y,"= ?")
        
        answer = input()
        
        while answer.isdigit() == False:
            if answer == "R" or answer == "r":
                rules.rules()
            elif answer == "S" or answer == "s":
                print("-"*60)
                print("Your current score is",cor,"out of",tot)
                print("You are currently on question #"+str(tot%5+1),"on round #"+str(math.ceil((tot+1)/5)))
                print("-"*60,"\n")
            else:
                print("Your input is invalid! Please try again.")
            print(x,"x",y,"= ?")
            answer = input()
                
        answer = int(answer)
        
        if answer == x*y:
            print("Congratulations! You are correct!\n")
            return True
        else:
            print("You are wrong! The correct answer is",str(x*y) + ".","\n")
            return False
