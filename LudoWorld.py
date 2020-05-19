from StartZone import StartZone
from Gatti import Gatti
import random as random


class LudoWorld:

    def __init__(self, num_players):
        self.players = random.sample(Gatti.colors.keys(), num_players)
        print(self.players)

        self.startZone = StartZone(self.players)

        self.turn = self.players.pop()

    def decide_turn(self):
        self.players.append(self.turn)
        self.turn = self.players.pop()

    def choose_gatti_to_play(self, gatti):
        gatti = gatti()
        random.randint(1, 4)

    def move_gatti(self):
        moves = random.randint(1, 6)
        # moves = 6
        self.playerColor = Gatti.colors[self.turn]
        for j in self.startZone.allGattis[Gatti.colors[self.turn]]:
            j.move(moves)
            self.startZone.check_other_gattis(j)

    def show_gatti_status(self):
        for i in self.startZone.allGattis:
            print(i)  # len(self.startZone.allGattis[i]))
            for j in self.startZone.allGattis[i]:
                print(j.loc)
