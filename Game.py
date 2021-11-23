
import time 
from GameMechanic import GameMechanics


class MathGame:
    
    def game(): #Loads questiosn and keeps track of answer and time

        questionTotal = 0 #stores # of questions
        answerTotal = 0 #stores # of right answers
        startTime = time.time() #chack to makesure play starts with 60 secounds
        index = 0 #Organizes the answer dict
        ansDict = dict() #stores answer to each function
         

        while time.time() - startTime <= 60: #Loop that will run till a minute is over

            index += 1
            function, correctAnswer = GameMechanics.function() #Loads answer and function 
            answer = input("The answer to {} is: ".format(function)) #Prints function

            try: #checks to see of answer is correct, return bolean value
                
                correct = (int(answer) == correctAnswer) 
            
            except:

                correct = False

            questionTotal += 1
            
            if correct:

                answerTotal += 1

            ansDict[index] = function, correctAnswer #Stores ordered tuple of function and answer

            print(f" {correct}! Time remaining is {60-(time.time() - startTime)}!")

        return answerTotal, questionTotal, ansDict 

    def gameMarks(results): #returns results be getting a tupple with answerTotal, questionTotal, and ans Dict in that order
        
        answer,question,ansDict = results
        ansRate = (answer/question) * 100 #gets correct rate
        print(f'''
        Thanks for playing! You were able to take on {question} questions

        Your correct rate is {round(ansRate,2)}%
        ''')

        seeAns = input("Would you like to see the answers for all the questions?(yes/no) ")

        if "yes" or "y" == seeAns.lower:

            for key, value in ansDict.items(): #Prints the answers to all the functions

                print(f"\n {key}) {value[0]} = {value[1]} ")

        print("Thank you for playing")






