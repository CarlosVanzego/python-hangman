# Hangman Game
# I am importing the 'random' module to generate a random word from the list of words I set. The random module is a python module that generates random numbers. It can be used to perform some random actions such a generating random number, randomizing the elements of a list, shuffling elements of a list, etc.
import random
# then from the 'collections' module I am importing the 'Counter' class. The Counter class is a subclass of the dictionary class. It is used to count the frequency of elements in a list. It is a part of the collections module which is a built-in Python module that implelements specialized container databases providing alternatives to Python's general purpose built-in containers like dict, list, set, amd tuple.
from collections import Counter
# I created the variable 'someWords' and assigned it a string of words. I used the triple quotes to allow me to write the string in multiple lines.
someWords = '''apple banana mango strawberry orange grape pineapple lemon coconut watermelon cherry raspberry peach blakckberry kiwi melon'''
# I then took 'someWords' and split it into a list of words using the split() method. The split() method splits a string into a list where each word is a list item.
someWords = someWords.split(' ')
# I created the variable 'word' and assigned it to a random word from the list of words using the random.choice() method. The random.choice method returns a randomly selected element from the specified sequence (in this case, the list of words).
word = random.choice(someWords)
# I made an if statement to check if the word is a fruit. If the word is a fruit, the game will start. If the word is not a fruit, the game will not start.
if __name__ == '__main__':
    # this print statement is to print the name of the game to the user.
    print('Guess the word! HINT: word is a name of a fruit')
    # this is a for loop that will print an underscore for each letter in the word. The end=' ' is used to print the underscores in the same line.
    for i in word:
        # this print statement will print an underscore for each letter in the word.
        print('_', end=' ')
    # this print statement is used to print a new line. 
    print()
    # this variable 'playing' is set to True. This is used to check if the game is still being played.
    playing = True
    # this variable 'letterGuessed' is set to an empty string. This is used to store the letters that the user has guessed.
    letterGuessed = ''
    # this variable 'chances' is set to the length of the word plus 2. This is the number of chances the user has to guess the word correctly.
    chances = len(word) + 2
    # this variable 'correct' is set to 0. This is used to store the number of correct guesses the user has made.
    correct = 0
    # this variable 'flag' is set to 0. This is used to check if the user has guessed the word correctly.
    flag = 0 
    # this try block is used to handle execeptions that may occur during the game like the user entering a number instead of a letter.
    try:
        # this while loop will run as long as the user still has chances to guess the word and the flag is not set to 1.
        while (chances != 0) and flag == 0:
            # this print statement is used to print the number of chamces the user has left.
            print()
            # chances is the number of chances the user has left.
            chances -= 1
            # this try block is used to handle exceptions that may occur when the user enters a letter.
            try:
                # the guess variable is used to store the letter the user enters, I assigned it to the input() method which will prompt the user to enter a letter.
                guess = str(input('Enter a letter to guess: '))
            # this execpt block is used to handle the exeception that may occur when the user enters a number instead of a letter. 
            except:
                # this print statement will print a message to the user telling them to enter only a letter.
                print('Enter only a letter!')
                # this continue statement is used to skip the rest of the code in the loop and go back to the start of the loop.
                continue
            # this if statement is used to check if the user entered a letter that is not an alphabet. 
            if not guess.isalpha():
                # this print statement will print a message to the user telling them to enter only a letter.
                print('Enter only a LETTER')
                # this continue statement is used to skip the rest of the code in the loop and go back to the start of the loop.
                continue
            # this elif statement is used to check if the user entered more than one letter.
            elif len(guess) > 1:
                # this print statement will print a message to the user telling them to enter only a single letter.
                print('Enter only a SINGLE letter')
                # this continue statement is used to skip the rest of the code in the loop and go back to the start of the loop.
                continue
            # this elif statement is used to check if the user entered a letter that has already been guessed.
            elif guess in letterGuessed:
                # this print statement will print a message to the user telling them that they have already guessed that letter.
                print('You have already guessed that letter')
                # this continue statement is used to skip the rest of the code in the loop and go back to the start of the loop.
                continue
            # this if statement is used to check if the letter the user entered is in the word.
            if guess in word:
                # I'm using the variable 'k' to store the number of times the letter the user entered is in the word. This is so that I can print the letter the number of times it appears in the word.
                k = word.count(guess)
                # this for loop is used to print the letter the number of times it appears in the word.
                for _ in range(k):
                    # I assigned the variable 'letterGuessed' to the letter the user entered.
                    letterGuessed += guess 

            # this for loop is used to print the word with the letters the user has guessed correctly.
            for char in word:
                # this if statement is used to check if the letter the user entered is in the word and the letter has not been guessed correcttly. I'm checking if 'char' is in 'letterGuessed' and the counter of 'letterGuessed' is not equal to the counter of 'word'.
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    # then I'm printing the letter the user entered.
                    print(char, end=' ')
                    # I am using the 'correct' variable to store the number of correct guesses the user has made, so i'm incrementing it by 1. 
                    correct += 1 
                # this elif statement is used to check if the letter the user entered is in the word and the letter has been guessed correctly. I'm checking if 'char' is in 'letterGuessed' and the counter of 'letterGuessed' is equal to the counter of 'word'.
                elif (Counter(letterGuessed) == Counter(word)):
                    # then I'm printing the string 'The word is: ' and the word.
                    print('The word is: ', end='')
                    # this prints the word.
                    print(word)
                    # the 'flag' variable is for checking if the user has guessed the word correctly, so i'm setting it to 1 to indicate that the user has guessed the word correctly.
                    flag = 1
                    # this print statement is used to print a message to the user telling them that they have won the game.
                    print('Congratulations, You won!')
                    # this break statement is used to break out of the loop.
                    break
                    # I have is twice because I want to break out of the for loop and the while loop.
                    break 
                # this else statement is used to print an underscore for each letter in the word that the user has not guessed correctly.
                else: 
                    # then I'm printing an underscore and a space.
                    print('_', end='')
        # this if statement is used to check if the user has run out of chances and has not guessed the word correctly.
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            # I'm printing a new line.
            print()
            # then printing a message to the user telling them that they have lost the game.
            print('You lost! Try again..')
            # then i'm printing the word to the user.
            print('The word was {}'.format(word)) 
    # this exepct block is used to handle the KeyboardInterrupt exception that may occur when the user presses 'Ctrl + C'. The KeyboardInterrupt exception is raised when the user presses 'Ctrl + C' to stop the program.
    except KeyboardInterrupt:
        # I'm printing a new line.
         print()
        # then printing a message to the user telling them bye and to try again.
         print('Bye! Try again.')
        # then I'm using the exit() method to terminate the program.
         exit()