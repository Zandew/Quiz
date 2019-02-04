import random

def round1():
        
    x,y = random.randint(1,100),random.randint(1,20)
    md = random.randint(0,1) #   0: multiply   1: divide
    if md == 1:
        while x % y != 0:
            x,y = random.randint(1,100),random.randint(1,30)
            
        print(x,"/",y,"= ?")
        
        answer = input()
        if answer == str(int(x/y)):
            return True
        else:
            return False
    elif md == 0:
        x,y = random.randint(2,20),random.randint(2,20)
        print(x,"x",y,"= ?")
        answer = int(input())
        if answer == x*y:
            return True
        else:
            return False

