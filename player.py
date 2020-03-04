"""
Player holds all the information of a OA player
"""

class Player:

    def __init__(self, number=None, name=None):
        self.number = int(number)
        self.name = name
        self.team = None
        self.data = None

        self.kills = {}
        self.killnumber = 0
        self.deathcount = 0
        self.killedby = {}
        self.weaponlist = {}

    def addkill(self, player):
        self.killnumber = self.killnumber + 1

        if not player in self.kills:
            self.kills[player] = 1
        else:
            self.kills[player] = self.kills[player] + 1
    
    def adddeath(self, player):
        self.deathcount = self.deathcount + 1

        if not player in self.killedby:
            self.killedby[player] = 1
        else:
            self.killedby[player] = self.killedby[player] + 1
    
    def weapons(self, weapon):
        if not weapon in self.weaponlist:
            self.weaponlist[weapon] = 1
        else:
            self.weaponlist[weapon] = self.weaponlist[weapon] + 1

    def mostkilled(self):
        try:
            return sorted(self.kills, key=self.kills.get, reverse=True)[0]
        except IndexError:
            return -1

    def favgun(self):
        try:
            return sorted(self.weaponlist, key=self.weaponlist.get, reverse=True)[0]
        except IndexError:
            return -1
            

            
