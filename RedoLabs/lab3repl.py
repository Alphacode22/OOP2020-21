class word_scrambler:
    def __init__(self):
        self.user_input = input("Please give me a sentence")

    def scramble(self):
        print("The user input was: ", self.user_input)

        sentence = self.user_input.strip().split()

        for index, word in enumerate(sentence):

            if len(word) > 3:
                temp_word = list(word)
                if(',' in temp_word) or ('.' in temp_word): # confusesd
                    temp = temp_word[1]
                    temp_word = temp_word[-3]
                    temp_word[-3] = temp

                else:
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-2]
                    temp_word[-2] = temp

                swapped_word = ''.join(temp_word)
                sentence[index] = swapped_word

            # else:

