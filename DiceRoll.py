import random


def generate_randomnumbers():
    return random.randrange(1, 7)



def get_only_six():
    dice_rolled = []
    while True:
        rand_number = generate_randomnumbers()
        print(rand_number)
        dice_rolled.append(rand_number)
        if rand_number == 6:
            print("Found number")
            break
    print("rolled \"{}\" time".format(len(dice_rolled)))




