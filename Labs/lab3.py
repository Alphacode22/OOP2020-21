# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string
# from os.path import split
# from re import split

def spliter(word):
    return [char for char in word]

class WordScramble:
    print("Start")

    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    # def join(word):
    #     return " ".join(word)

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # # Error checking
        # if not self.user_input.isascii():
        #     print("Your input was not a string!!!!")
        #     return


        # first scramble is just one word
        ourWord = spliter(self.user_input)
        # print(spliter(self.user_input))

        # ourWord = []

        # for word in self.user_input.split():
        #     ourWord.append(word)
        #     print(word)

        temp = ourWord[0]
        ourWord[0] = ourWord[1]
        ourWord[1] = temp

        print(ourWord)

        # reverse two indices

        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a word that is longer than 3


        if len(ourWord) > 3:
            temp = ourWord[0]
            ourWord[0] = ourWord[-1]
            ourWord[-1] = temp

            temp = ourWord[1]
            ourWord[1] = ourWord[-2]
            ourWord[-2] = temp

        # ourWord = ''.join(ourWord)

        newWord = ''

        for letter in ourWord:
            newWord += letter

        print(newWord)
        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation


word_scrambler = WordScramble()
word_scrambler.scramble()
print("Done")


# print(temp_word)

# for word in self.user_input.split():
#     for letter in self.user_input.split():
#         self.user_input[0] = self.user_input[-1]




# temp = temp_word[1]
# temp_word[1] = temp_word[-3]
# temp_word[-3] = temp

# temp_word = "Hello"

# # # # newWord = self.user_input

# # # sentence = [self.user_input]

# temp_word = [self.user_input]


##Move the first letter of every word in the input sentence to the end of that word and the add on ‘ay’
##stringInput = input("Enter a string")
##for word in stringInput.split():
##    for letter in word:
##        word[0] = word[-1]

# print(sentence[::2])

# # Move the first letter of every word in the input sentence to the end of that word and the add on ‘ay’
# for word in self.user_input.split():
#    for letter in word:
#        word[0] = word[-1]


# box = "Cavan"
# printOut = box[0] + box[1]
# print(printOut)
# print(box[0] + box[4])
#
# box1 = " CIFLEORVFEGCHOIDIIGNHG"
# print(box1[::2])

# vowels = "aeiou"
# output = ""
# testMe = "She sat under the table"

# for char in testMe:
#     print("loop")
#     output = output + char
#     if char in vowels:
#         output += "eg"
#
# print(output)
#

