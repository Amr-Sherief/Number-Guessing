import random

infinite = [0 , 0 , 0 , 0]

small_numbers = [1, 2, 3]

try:
    number_of_retries = input()

    for i in range(int(number_of_retries)-1):
        number_of_retries.insert(0)


    insert = input()                                  #the insert of the player
    insert = insert.split(" ")

    first = int(insert[0])                            #the first number of the guessing range
    second = int(insert[1])                           #the second number of the guessing range

    guessing_numbers = range(first, second)           #the guessing range
    number = random.choice(guessing_numbers)          #the random number that the player should guess

                                                      #the player's guess of the number
    for i in number_of_retries:
        small_guess = random.choice(small_numbers)
        small_guess_2 = random.choice(small_numbers)
        try_1 = input()
        if int(try_1) == number:  # Tells the player that he/she guessed right
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
            print("Stupid")
            break
        elif 1 < second - first < 6 and ((second - 1) - (first + 1)) != 0 and number in range((first+1),(second-1)):  # Acts on numbers of difference between 1 and 6
            print("Number is between " + str(first + 1) + " " + str(second - 1))  # Gives the player a hint
            first = first + 1
            second = second -1
            continue
        elif second - first == 6 and number in range((first+2),(second-2)):  # Acts if the difference between the numbers is 6
            print("Number is between " + str(first + 2) + " " + str(second - 2))
            first = first + 2
            second = second - 2
            continue
        elif 7 == second - first and number in range((first+1),(second-1)):                          # Acts if the difference between the numbers is 7
            print("Number is between " + str(first + 1) + " " + str(second - 2))
            first = first + 1
            second = second - 2
            continue
        elif 7 < second - first < 10 and number in range((first+small_guess),(second-small_guess_2)): #Acts if the difference between the two numbers is between 7 and 10
            print("Number is between " + str(first + small_guess) + " " + str(second - small_guess_2))
            first = first + small_guess
            second = second - small_guess_2
            continue
        else:  # prints the number if no conditions returned true
            print("The number is " + str(number))
    else:                                                           #Acts if the loop ends
        print("\nThe number is " + str(number))


except ValueError:
    print("Insert digits ONLY")
 #todo add an input so the player decides the number of retries