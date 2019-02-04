import random

def r1():
        
    x,y = random.randint(1,100),random.randint(1,20)
    md = random.randint(0,1) #   0: multiply   1: divide
    if md == 1:
        while x % y != 0:
            x,y = random.randint(1,100),random.randint(1,30)
            
        print(x,"/",y,"= ?")
        
        answer = input()
        
        while type(answer) is not int:
            if answer == "R" or answer == "r":
                rule()
            elif answer == "S" or answer == "s":
                score()
            else:
                print("Your input is invaild! Please try again.")
            print(x,"/",y,"= ?")
            answer = input()
        if answer == str(int(x/y)):
            print("Congratulations! You are correct!")
            return True
        else:
            print("You are wrong! The correct answer is",int(x/y))
            return False
    elif md == 0:
        x,y = random.randint(2,20),random.randint(2,20)
        print(x,"x",y,"= ?")
        answer = int(input())
        if answer == x*y:
            print("Congratulations! You are correct!")
            return True
        else:
            print("You are wrong! The correct answer is",x*y)
            return False

