import Wordliste
import random


def menu():
    return input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')


def main_module(win, lost):
    N = random.choice(Wordliste.wörter)
    Word = N
    word = '-' * len(N)
    print(word)
    N = list(N)
    attempts = 0
    guessed_w = set()
    while attempts < 8:
        print()
        W = input('Input a letter:')
        if not W.islower() or len(W) != 1 or not W.isalpha():
            print(word)
            print('please, enter a lowercase letter from the English alphabet.')
            print("Please, input a single letter.")
            continue
        if W in guessed_w:
            print(word)
            print("You've already guessed this letter.")
        elif W in N:
            for i in range(len(N)):
                if N[i] == W:
                    word = word[:i] + W + word[i + 1:]
            guessed_w.add(W)
            print(word)
            if word == Word:
                print(word)
                print(f"You guessed the word {word}!")
                print('You survived!')
                win += 1
                break
        else:
            print(word)
            print("That letter doesn't appear in the word.")
            guessed_w.add(W)
            attempts += 1
            if attempts == 8:
                lost += 1
                print('You lost!')
                break

    return win, lost


print('H A N G M A N')
print('The game will be available soon.')
win = 0
lost = 0
while True:
    start = menu()
    if start == "play":
        win, lost = main_module(win, lost)
    elif start == "results":
        print(f"You won: {win} times")
        print(f"You lost: {lost} times")
    elif start == "exit":
        break

print('Thanks for playing!')
