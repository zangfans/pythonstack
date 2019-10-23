#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/10/22
def hangman(word):
    wrong = 0
    stages = ["",
               "----------------",
               "|  |            ",
               "|  |            ",
               "|  0            ",
               "| /|\           ",
               "| / \           ",
               "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter> "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("Your win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Your lose! Tt was {}.".format(word))

hangman("cat")

if __name__=="__main__":
    hangman("cat")