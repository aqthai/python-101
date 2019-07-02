#
# Author: Alvin Thai
# Description:
#     Hangman game that uses list casting, lists, join method, while loop, and for loop.  Player 1 inputs a word and player 2 guesses letters of the word until the word is guessed correctly.
#
def hangman():
    print("HANGMAN: Welcome to HANGMAN!")
    word = input("HANGMAN: player 1 Enter a hangman word: ")
    word_letters = list(word)
    guesses = 6
    used_letters = set()
    underline = str("_" * len(word))
    underscores = list(underline)
    str_underscores = ''.join(underscores).strip()
    while guesses > 0 and str_underscores != word:
        print("HANGMAN: Wrong guesses left:  " + str(guesses))
        # turns the list underscores into a string each round a letter is guessed then shows progress
        str_underscores = ''.join(underscores).strip()     
        print("HANGMAN: Word progress: " + str(str_underscores))      
        if str(str_underscores) == word:
            print("HANGMAN: player 2 wins!")
            break 
        letter = input("HANGMAN: player 2 guess a letter: ")
        if letter in used_letters:
            print("HANGMAN: You already guessed \'" + str(letter) + "\'")         
        elif letter in word_letters:
            for i in range(0, len(word)):       # changes elements in underscores to a letter in word at each index
                if word[i] == letter:
                    underscores[i] = letter
            print("HANGMAN: YES!")
            used_letters.add(letter)          
        elif letter not in word_letters:
            print("HANGMAN: NOPE!")
            guesses -= 1
            used_letters.add(letter)
    if guesses == 0:
        print("HANGMAN: Wrong guesses left:  " + str(guesses))
        print("HANGMAN: Word progress: " + str(underline))
        print("HANGMAN: player 1 wins!")
def main():        
    hangman()
main()