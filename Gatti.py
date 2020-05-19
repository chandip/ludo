<<<<<<< HEAD
=======

>>>>>>> 40caa8ad9c865127d49836dbbb122b9dd0568e5f
## This class is for the gatti
class Gatti:
    colors = {0: "red", 1: "green", 2: "yellow", 3: "blue"}

    loc = -1
<<<<<<< HEAD
    max_moves = 56
    in_safe_zone = True
    safe_zones = [-1, 0, 8, 13, 21, 26, 34, 39, 47]
    home_zones = [51, 52, 53, 54, 55, 56]

    def __init__(self, color):
        self.color = color
        self.loc = -1

    def move(self, num_moves):
        # If the gatti is at its start position
        if self.loc < 0:
            # Gatti needs a 6 to move out from start position
            if num_moves == 6:
                print("Its a six!")
                self.loc += 1
            # Do nothing if its not a six
            else:
                print("Its not a six! Still Stuck!")
                # self.loc+=num_moves
        # if it is not a six
        elif self.loc + num_moves <= Gatti.max_moves:
            self.loc = self.loc + num_moves
        else:
            print("here")
            # pass

        # in_safe_zone=self.isin_safe_zone()
=======
    MAXMOVES = 56
    inSafeZone = True
    SAFEZONES = [-1, 0, 8, 13, 21, 26, 34, 39, 47]
    HOMEZONES = [51, 52, 53, 54, 55, 56]

    def __init__ (self, color):
        self.color = color
        self.loc = -1

    def move(self, numMoves):
        # If the gatti is at its start position
        if self.loc < 0:
            # Gatti needs a 6 to move out from start position
            if numMoves == 6:
                print("Its a six!")
                self.loc+=1
            # Do nothing if its not a six
            else:
                print("Its not a six! Still Stuck!")
                #self.loc+=numMoves
        # if it is not a six
        elif self.loc + numMoves <= Gatti.MAXMOVES:
            self.loc = self.loc + numMoves
        else:
            print("here")
            #pass

        #inSafeZone=self.isInSafeZone()
>>>>>>> 40caa8ad9c865127d49836dbbb122b9dd0568e5f
