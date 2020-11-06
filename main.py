import random

try:
    insert = input()
    insert = insert.split(" ")

    first = int(insert[0])
    second = int(insert[1])

    guessing_numbers = range(first, second)
    number = random.choice(guessing_numbers)

    try_1 = input()

    if try_1 == number:
        print("Congratulations")
except ValueError:
    print("Insert digits ONLY")
