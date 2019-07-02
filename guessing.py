#
# Author: Alvin Thai
# Description:
#     Forms a guessing game between two players using inputs, if statements, lists, for and while loops and append.  Player one submits an integer into an input and the player two guesses until the number is correct.  Every guess adds into a list and the results are printed out after the other player guesses the right number.
#
maximum = 100
# A maximum limit to the guessing game is established by this variable.  It can be adjusted.
def guessing():
    print("Welcome to the guessing game!")
    print()
    count = 0
    guesses = []
    number = int(input("Player 1: Enter number for Player 2 to guess between 0 and " 
                       + str(maximum) + ": "))
    while number < 0 or number > maximum:
        if number < 0:
            print("  That number is less than zero!")
            number = int(input("Player 1: Enter number for Player 2 to guess between 0 and 100: "))
# Another input function is used to continue the while loop until an integer within the determined range is used.  This allows another number to be used for the while loop.
        if number > maximum:
            print("  That number is greater than " + str(maximum)+ "!")
            number = int(input("Player 1: Enter number for Player 2 to guess between 0 and " 
                               + str(maximum) + ": "))
    print()
    guess = int(input("Player 2, guess a number: "))
# The input guess is run through an if-else statement which adds to the variable count and appends to the list guesses
# The input guess is compared with the number Player 1 chose and this determines what prints out.
    if guess == number:
        count += 1
        guesses.append(guess)
        print("Correct!")
        print("You got it right in " + str(count) + " guess! Wow, you are AMAZING.") 
        print()     
    else:
        while guess != number:
            if guess < number:
                print("Too low...")
                count += 1
                guesses.append(guess)
                guess = int(input("Player 2, guess a number: "))
                #The next guess continues the while loop.
            elif guess > number:
                print("Too high...")
                count += 1
                guesses.append(guess)
                guess = int(input("Player 2, guess a number: "))
            elif guess < 0:
                print("The number is less than 0!")
                count += 1
                guesses.append(guess)
                guess = int(input("Player 2, guess a number: "))
            elif guess > 100:
                print("The number is greater than 100!")
                count += 1
                guesses.append(guess)
                guess = int(input("Player 2, guess a number: "))
        if guess == number:
            print("Correct!")
            count += 1
            guesses.append(guess)
            print()
    return count, guesses
# The next function uses returned variables count and guesses locally with generic variables a and b.
def statistics(a, b):
    print("It took you " + str(a) + " tries to guess correctly!")
    print("The numbers you guessed were: ", end="")    # end="" continues the statement on the same line.
    for guess in b:
        print(str(guess) + " ", end="")
# The for loop prints each element of the list assigned to variable b and is followed by , end="" to continue through each one on the same line.  It is followed by an empty print statement to go onto the next line.
    print()
    print("Goodbye!")    
# The values stored in the first function under main are assigned different variables again.  The variables used will not change the output of the main function, because it runs at a different scope. 
def main():
    x, y = guessing()
    statistics(x, y)
    
main()
    
          