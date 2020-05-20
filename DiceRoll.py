import random


def generate_randomnumbers():
    return random.randrange(1, 7)


def get_only_six():
    dice_rolled = []
    gatti_move = []
    while True:
        x = input('Roll Dice By pressing anykey...')
        rand_number = generate_randomnumbers()
        print(x)
        print("you have number: " + str(rand_number))
        dice_rolled.append(rand_number)
        if rand_number == 6:
            print("+++++++++++++++++++++++++++++")
            print("You can now spawn your Gatti")
            print("+++++++++++++++++++++++++++++\n")
            # gatti_move.append(0)
            while True:
                x = input('Press any key to roll Dice and move gatti..')
                after_spawn_rand_number = generate_randomnumbers()
                print(x)
                print("you have number: " + str(after_spawn_rand_number))
                gatti_move.append(after_spawn_rand_number)
                print("total number: {} \n".format(sum(gatti_move)))
                if sum(gatti_move) > 40:
                    print("+++++++++++++++++++++++++")
                    print("You reached the max move")
                    print("+++++++++++++++++++++++++\n")
                    print(sum(gatti_move))
                    break
            break

        print("rolled \"{}\" time \n".format(len(dice_rolled)))

