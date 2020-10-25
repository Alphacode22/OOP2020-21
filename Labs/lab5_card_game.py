# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 5 - GUI and card game using queue
import queue
from tkinter import *

# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle

# import random
from random import randint

# import a file operator
import os


# Label
# Card image
# Shuffling card may need queues - pop first card push temp card to back
# Other functions not done



class CardGame():

    # initialises the application
    def __init__(self):
        # set up game logic here:
        # shuffle the cards before first use
        # variable for holding the score
        self.player_score = 0
        self.the_cards = self.load_cards()
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        root = Tk()
        root.geometry("300x200")
        root.title("Card Game")

        master_frame = Frame(master=root)
        master_frame.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(master=master_frame)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(master=master_frame)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(master=master_frame)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        self.open_card = Button(cards_frame)
        the_card = PhotoImage(file='cards/queen_hearts.gif')
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        closed_deck = Button(cards_frame, command=self.pick_card)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!", command=self.check_scores)
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.reset_game)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score), justify=LEFT)
        self.score_label.pack()

        root.mainloop()

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    # helper function to load the cards
    # puts everything in a list first as it needs to be shuffled
    # returns a queue
    def load_cards(self):
        print("\nLoad cards")
        # cards = Queue(maxsize=52) #change this if you want to use a different data structure
        cards= []
        # suits = ("hearts", "diamonds", "spades", "clubs")
        # people = ("queen", "jack", "king")

        path = "C:\\Users\\AlexZ\\PycharmProjects\\Lab1\\OOP2020-21\\Labs\\cards"
        files = os.listdir(path)
        for f in files:
            if f != "closed_deck.gif":
                cards.append(f)
                # cardsList.append(f)
            #print(f)
        shuffle(cards)
        # [cards.put(i) for i in cardsList]

        print(cards)
        # print(len(cards))
        # pickedCard = cards[0]
        # print("\n" + pickedCard)
        return cards

    # called when clicking on the closed deck of cards
    # picks a new card from the card FIFO
    # updates the display
    # updates the score
    def pick_card(self):
        print("\nPick card")
        # pickedCard = self.the_cards.dequeue(1)
        # self.the_cards[-1].put(pickedCard)
        pickedCard = self.the_cards.pop(0)
        self.the_cards.append(pickedCard)
        # the_card = PhotoImage(file=f'cards/{pickedCard}')
        print(pickedCard)
        print(len(self.the_cards))
        self.open_card.photo = pickedCard
        self.update_score(pickedCard)


    # contains the logic to compare if the score
    # is smaller, greater or equal to 21
    # sets a label
    def check_scores(self):
        print("\nCheck score")
        if self.player_score < 21:
            # smaller than 21
            # self.score_label = Label(score_frame, text="Your score: " + str(self.player_score) + "You win, play again?", justify=LEFT)
            self.score_label.text = "Your score: " + str(self.player_score) + "You win, play again?"
        elif self.player_score > 21:
            # greater than 21
            # self.score_label = Label(score_frame, text="Your score: " + str(self.player_score) + "You lose, play again?", justify=LEFT)
            self.score_label.text = "Your score: " + str(self.player_score) + "You lose, play again?"
        elif self.player_score == 21:
            # equal to 21
            # self.score_label = Label(score_frame, text="Your score: " + str(self.player_score) + "You hit the jack pot!", justify=LEFT)
            self.score_label.text = "Your score: " + str(self.player_score) + "You hit the jack pot!"

    # calculates the new score
    # takes a card argument of type
    def update_score(self, card):
        print("\nUpdate Score")
        if "10" in card:
            self.player_score += 10
        elif "1" in card:
            self.player_score += 1
        elif "2" in card:
            self.player_score += 2
        elif "3" in card:
            self.player_score += 3
        elif "4" in card:
            self.player_score += 4
        elif "5" in card:
            self.player_score += 5
        elif "6" in card:
            self.player_score += 6
        elif "7" in card:
            self.player_score += 7
        elif "8" in card:
            self.player_score += 8
        elif "9" in card:
            self.player_score += 9
        elif "jack" in card or "queen" in card or "king" in card:
            self.player_score += 10
        print(self.player_score)

    # this method is called when the "Done" button is clicked
    # it means that the game is over and we check the score
    # but we don't allow any further game play. When clicking
    # on the closed deck after this button is pressed, nothing
    # should happen. Only options are to ask for a new game or
    # exit the program after this button was pressed.
    def done_playing(self):
        pass  # replace this line by your code

    # this method is called when the "New Game" button is clicked
    # resets all variables
    # sets the game's cards to the initial stage, with a freshly
    # shuffled card deck
    def reset_game(self):
        # trying this
        self.player_score = 0
        self.init_window()



# object creation here:

app = CardGame()
