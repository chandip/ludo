import random


def randomnumbers():
    r = random.randrange(1, 7)
    return r


def get_only_six():
    while True:
        rand_number = randomnumbers()
        print(rand_number)
        if rand_number == 6:
            print("got the number")
            break


