import round1, round2, round3, random, math, rules

def main():

    '''
    Parameter: No parameters
    Purpose:   Starts the Math Quiz
    Return:    No return value (returns None)
    '''
    
    # Greets the user
    print("Welcome to the FUN MATH QUIZ!\n")

    # Explanation of the game to the user
    print("There will be 3 rounds in total and 5 questions in each round:")
    print("Round 1:\tMultiply & Divide")
    print("Round 2:\tSolving Quadratic Equations")
    print("Round 3:\tSolving Right Triangles")

    # Outputs the rules to the user
    rules.rules()

    # User is prompted to enter anything to start the game
    print("ARE YOU READY TO START?? (Enter anything to start the game)")
    input()

    # Original number of questions user answered correctly and number of questions the user has answered
    score = 0
    questions = 0

    # Round #1
    print("ROUND 1 BEGIN")
    
    # 5 questions for Round 1
    for i in range(5):
        print("ROUND 1 QUESTION "+str(i+1)+"\n")
        
        # Round 1 function call
        if (round1.r1(score, questions)):
            
            # If the user answered the question correctly, the number of questions answered correctly increases by 1
            score += 1

        # The number of questions the user answered increases by 1 each time
        questions += 1

    # Round #2
    print("ROUND 2 BEGIN")
    
    # 5 questions for Round 2
    for i in range(5):
        
        print("ROUND 2 QUESTION "+str(i+1)+"\n")

        # Round 2 function call
        if (round2.r2(score, questions)):
            
            # If the user answered the question correctly, the number of questions answered correctly increases by 1
            score += 1

        # The number of questions the user answered increases by 1 each time
        questions += 1

    # Round #3
    print("ROUND 3 BEGIN")
    
    # 5 questions for Round 3
    for i in range(5):
        
        print("ROUND 3 QUESTION "+str(i+1)+"\n")
        
        # Round 3 function call
        if (round3.r3(score, questions)):
            
            # If the user answered the question correctly, the number of questions answered correctly increases by 1
            score += 1

        # The number of questions the user answered increases by 1 each time
        questions += 1

    # Outputs the final score of the user
    print("\nYour final score is",score,"out of",questions)
    
main()
