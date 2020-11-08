import random

infinite = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

small_numbers = [1, 2]
small_guess = random.choice(small_numbers)
small_guess_2 = random.choice(small_numbers)
try:
    insert = input()                                  #the insert of the player
    insert = insert.split(" ")

    first = int(insert[0])                            #the first number of the guessing range
    second = int(insert[1])                           #the second number of the guessing range

    guessing_numbers = range(first, second)           #the guessing range
    number = random.choice(guessing_numbers)          #the random number that the player should guess

                                                      #the player's guess of the number
    for i in infinite:
        try_1 = input()
        if try_1 == number:  # Tells the player that he/she guessed right
            print("Congratulations You got it right")
            break
        elif first > second:  # Tells the player that second must be greater than first
            print("Second number should be greater than first number")
            continue
        elif second - first == 0:  # Tells the player that second must be greater than first
            print("Second number should be greater than first number")
            continue
        elif second < 0 or first < 0:  # Tells the player that there should be no negative number
            print("There should be no negative numbers")
            continue
        elif 1 == second - first:  # Tells the player the random number
            print("Number is " + str(number))
            print("Good luck next time")
            break
        elif 1 < second - first < 6 and (
                (second - 1) - (first + 1)) != 0:  # Acts on numbers of difference between 1 and 6
            print("Number is between " + str(first + 1) + " " + str(second - 1))  # Gives the player a hint
            print("Try Again:")  # todo: see the condition if str(first+1) + " " + str(second-1) == 1
            try_2 = input()
            if try_2 == number:  # Sees if the player guessed the second time right
                print("Congratulations You got it right")
            elif try_2 != number and ((second - 2) - (first + 2)) != 0:
                print("Number is between " + str(first + 2) + " " + str(second - 2))  # Gives the player a hint
                print("Try Again:")
                try_3 = input()
                if try_3 == number:  # Sees if the player guessed the third time right
                    print("Congratulations You got it right")
            else:
                print("The number is " + str(number))
        elif second - first == 6:  # Acts if the difference between the numbers is 6
            print("Number is between " + str(first + 2) + " " + str(second - 2))
            continue
        elif 6 < second - first < 10:  # Acts if the difference between the numbers is between 6 and 10
            print("Number is between " + str(first + small_guess) + " " + str(second - small_guess_2))
            continue
        else:  # prints the number if no conditions returned true
            print("The number is " + number)


except ValueError:
    print("Insert digits ONLY")
