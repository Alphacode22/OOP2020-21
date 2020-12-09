# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a word: ")

    def scramble(self):
        # # print what was input
        # print("The user input was: ", self.user_input)
        #
        # # first scramble is just one word
        # # reverse two indices
        # # particularly good to use is to switch the first two
        # # and the last two
        # # this only makes sense if you have a world that is longer than 3
        # l = list(self.user_input)
        #
        # temp = l[0]
        # l[0] = l[1]
        # l[1] = temp
        #
        # if len(l) > 3:
        #     temp = l[-1]
        #     l[-1] = l[-2]
        #     l[-2] = temp
        #
        # l = ''.join(l)         #''.join
        # print(l)

        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        # sentence = self.user_input.strip().split()
        #
        # for i, word in enumerate(sentence):
        #     temp_word = list(word)
        #
        #     if(',' in temp_word or '.' in temp_word):
        #         temp_word = word[0]
        #         word[0] = word[1]
        #         word[1] = temp_word
#===================================================================
        sentence = self.user_input.strip().split()

        for i, word in enumerate(sentence):
            #Converts word into letters
            letters = list(word)

            if len(word) > 3:
                if(',' in letters) or ('.' in letters):
                    temp = letters[1]
                    letters[1] = letters[-3]
                    letters[-3] = temp
                else:
                    temp = letters[1]
                    letters[1] = letters[-2]
                    letters[-2] = temp

                newWord = ''.join(letters)
                sentence[i] = newWord

            else:
            # Since the length of the word < 3 don't swap the word
                sentence[i] = word

        print(sentence)

word_scrambler = WordScramble()
word_scrambler.scramble()

