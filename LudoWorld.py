from StartZone import StartZone
from Gatti import Gatti
import random as random


class LudoWorld:

<<<<<<< HEAD
    def __init__(self, num_players):
        self.players = random.sample(Gatti.colors.keys(), num_players)
=======
    def __init__(self, numPlayers):
        self.players = random.sample(Gatti.colors.keys(), numPlayers)
>>>>>>> 40caa8ad9c865127d49836dbbb122b9dd0568e5f
        print(self.players)

        self.startZone = StartZone(self.players)
        print(self.startZone)

        self.turn = self.players.pop()
        print(self.turn)

<<<<<<< HEAD
    def decide_turn(self):
        self.players.append(self.turn)
        self.turn = self.players.pop()

    def choose_gatti_to_play(self, gatti):
        gatti = gatti()
        random.randint(1, 4)

    def move_gatti(self):
=======
    def decideTurn(self):
        self.players.append(self.turn)
        self.turn = self.players.pop()

    def chooseGattiToPlay(self, gatti):
        gatti = gatti()
        random.randint(1, 4)

    def moveGatti(self):
>>>>>>> 40caa8ad9c865127d49836dbbb122b9dd0568e5f
        moves = random.randint(1, 6)
        # moves = 6
        self.playerColor = Gatti.colors[self.turn]
        for j in self.startZone.allGattis[Gatti.colors[self.turn]]:
            j.move(moves)
<<<<<<< HEAD
            self.startZone.check_other_gattis(j)

    def show_gatti_status(self):
=======
            self.startZone.checkOtherGattis(j)

    def showGattiStatus(self):
>>>>>>> 40caa8ad9c865127d49836dbbb122b9dd0568e5f
        for i in self.startZone.allGattis:
            print(i)  # len(self.startZone.allGattis[i]))
            for j in self.startZone.allGattis[i]:
                print(j.loc)
