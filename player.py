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
        self.weaponlist = {}

    def addkill(self, player):
        self.killnumber = self.killnumber + 1

        if not player in self.kills:
            self.kills[player] = 1
        else:
            self.kills[player] = self.kills[player] + 1
        
        
    
    def weapons(self, weapon):
        if not weapon in self.weaponlist:
            self.weaponlist[weapon] = 1
        else:
            self.weaponlist[weapon] = self.weaponlist[weapon] + 1
        
            

            
