"""


[10:07 AM] Bryan Duggan
    well u should start by making the abstract class with the abstract methods
​[10:08 AM] Bryan Duggan
    and then make the fibonacchi class extend the abstract class
​[10:08 AM] Bryan Duggan
    and implement the abstract methods
​[10:09 AM] C19409486 Alex Bang


"""
import abc
class Maths:

    @abc.abstractmethod
    def __init__(self):
        pass

    @property
    def user_input_property(self):
        return

    @abc.abstractmethod
    def play_game(self):
        print("Welcome to this game")

class MathsGames(Maths):
    # global variable

    def __init__(self):
        super().__init__()

    def play_game(self):
        guessMe = self.fibonacci()
        print("What is the next number?")
        userGuess = self.userGuess()
        if userGuess == guessMe:
            print("You win")
        else:
            print("You lose")

    def fibonacci(self):
        maxNumber = int(input("Enter the max number of fib: "))
        previousNumber = 0
        nextNumber = 1
        fibArray = []
        guessMe = 0

        for i in range(0, maxNumber):
            sum = previousNumber + nextNumber
            previousNumber = nextNumber
            nextNumber = sum
            fibArray.append(sum)
            guessMe = previousNumber + nextNumber

        print(fibArray)
        return guessMe


    def userGuess(self):
        userGuess = int(input("Your ans is: "))
        return userGuess


mg = MathsGames()
mg.play_game()






