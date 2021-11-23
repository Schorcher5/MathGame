import random

class GameMechanics: #generates the function and its answer

    def function():

        operator = ["/", "+", "*", "-"]#The operators the program will use
        a = random.randint(1, 99) #uses random to pick two numbers between 1 and 99
        b = random.randint(1, 9)
        op = random.choice(operator) #picks a random operator
        function = "{}{}{}".format(a,op,b) #forms the function
        answer = int(eval(function)) #gets the answer

        return function, answer









