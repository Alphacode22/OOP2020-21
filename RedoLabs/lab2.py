#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #

        # print only first and last of the sentence:
        print(message[0], message[-1])

        # use slice notation:
        print(message[:0:] + message[:-1:])


        # escaping a character:
        print("\n")


        # find all a's in the input word and count how many there are:
        count=0
        for i in message: # wrong
            if i == 'a':
                count += 1
        print(count)

        print(message.count('a'))
        # replace all occurences of the character a with the - sign
        for i in message:
            if i == 'a':
                i = '-'
        print(message)

        #print(message)
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():

        print(message.replace('a', '-'))

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        message = list(message)

        # append a new element to the list and print:
        message.append("Emer")

        # remove from the list in 3 ways:
        print(message.remove("Emer"))
        del message[2]
        print(message)

        print(message.pop())

        # check if the word cake is in your input list:
        if "cake" in message:
            print("Yes")

        # reverse the items in the list and print:
        print(message.reverse())

        # reverse the list with the slicing trick:
        print(message[::-1])

        # print the list 3 times by using multiplication:
        print(message * 3)


tas = Types_and_Strings()
tas.play_with_strings()
#tas.play_with_lists()
