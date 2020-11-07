import random

small_numbers = [2, 3, 4]
try:
    insert = input()                                  #the insert of the player
    insert = insert.split(" ")

    first = int(insert[0])                            #the first number of the guessing range
    second = int(insert[1])                           #the second number of the guessing range

    guessing_numbers = range(first, second)           #the guessing range
    number = random.choice(guessing_numbers)          #the random number that the player should guess

    try_1 = input()                                   #the player's guess of the number

    if try_1 == number:                               #Tells the player that he/she guessed right
        print("Congratulations You got it right")
    elif first > second:                              #Tells the player that second must be greater than first
        print("Second number should be greater than first number")
    elif second - first == 0:                         #Tells the player that second must be greater than first
        print("Second number should be greater than first number")
    elif second < 0 or first < 0:                     #Tells the player that there should be no negative number
        print("There should be no negative numbers")
    elif 1 == second - first:                         #Tells the player the random number
        print("Number is" + str(number))
        print("Good luck next time")
    elif 1 < second - first < 6 and ((second-1) - (first+1)) != 0:         #Acts on numbers between 1 and 6
        print("Number is between" + str(first+1) + " " + str(second-1))    #Gives the player a hint
        print("Try Again:")                                                #todo: see the condition if str(first+1) + " " + str(second-1) == 1
        try_2 = input()
        if try_2 == number:                                                # Sees if the player guessed the second time right
            print("Congratulations You got it right")
        elif try_2 != number and ((second-2) - (first+2)) != 0:
            print("Number is between" + str(first+2) + " " + str(second-2)) #Gives the player a hint
            print("Try Again:")
            try_3 = input()
            if try_3 == number:                                             #Sees if the player guessed the third time right
                print("Congratulations You got it right")
        else:
            print("The number is " + str(number))
    else:                                                                   #prints the number if no conditions returned true
        print("The number is " + str(number))

except ValueError:
    print("Insert digits ONLY")
