import random, rules, math

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
                print("Your current score is",cor,"out of",tot)
                print("You are currently on question #"+str(tot%5+1),"on round #"+str(math.ceil((tot+1)/5)))
            else:
                print("Your input is invalid! Please try again.")
            print(x,"/",y,"= ?")
            answer = input()
        if answer == str(int(x/y)):
            print("Congratulations! You are correct!\n")
            return True
        else:
            print("You are wrong! The correct answer is",int(x/y),"\n")
            return False
    elif md == 0:
        x,y = random.randint(2,20),random.randint(2,20)
        print(x,"x",y,"= ?")
        
        answer = input()
        
        while answer.isdigit() == False:
            if answer == "R" or answer == "r":
                rules.rules()
            elif answer == "S" or answer == "s":
                print("Your current score is",cor,"out of",tot)
                print("You are currently on question #"+str(tot%5+1),"on round #"+str(math.ceil((tot+1)/5)))
            else:
                print("Your input is invalid! Please try again.")
            print(x,"x",y,"= ?")
            answer = input()
                
        answer = int(answer)
        
        if answer == x*y:
            print("Congratulations! You are correct!\n")
            return True
        else:
            print("You are wrong! The correct answer is",x*y,"\n")
            return False

