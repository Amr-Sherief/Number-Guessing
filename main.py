import random

try:
    insert = input()
    insert = insert.split(" ")

    first = int(insert[0])
    second = int(insert[1])

    guessing_numbers = range(first, second)
    number = random.choice(guessing_numbers)
except ValueError:
    print("Insert digits ONLY")
