"""
Parser handles reading and interpreting the OA logfile
"""

from player import Player

class Parser:
    

    def __init__(self, logfile):
        self.logfile = logfile
        self.loglist = []
        self.log = []
        self.players = {}

        self.open()
        self.get_timecodes()
        self.get_commands()
        self.get_players()
        self.get_kills()

        self.results()

        self.guns = {
            1: "Shotgun",
            3: "Machinegun",
            7: "",
            8: "",
            10: "Railgun",
            20: "Suicide",
        }

    def open(self):
        try:
            f = open(self.logfile)
            for line in f:
                self.loglist.append(line)
        except IOError:
            print("File", self.logfile, "not found!")
    
    def get_timecodes(self):
        for i in self.loglist:
            self.log.append(i[7:].strip())
    
    def get_commands(self):
        #remove = []
        temp = []
        for i in self.log:
            #print(i)
            try:
                temp.append(i.split(":", 1))
            except IndexError:
                print(i)
                pass
        print("Commands extracted")
        #for i in remove:
        #    self.log.pop(i)
        self.log = temp

    def get_players(self):
        print("Getting players from log size of", len(self.log))
        for i in self.log:
            if i[0] == "ClientUserinfoChanged":
                temp = i[1].split("n\\", 1)
                #print("Found", temp[1].split("\\"))
                playernumber = int(temp[0].strip())
                if playernumber > 30: continue
                self.players[playernumber] = Player(number=playernumber)
                self.extract_player_data(self.players[playernumber], temp[1].split("\\"))
        #for i in self.players:
        #    print(self.players[i].number, self.players[i].name)
        #print(self.players)

    def get_kills(self):
        for i in self.log:
            if i[0] == "Kill":
                data = i[1].split(":", 1)[0].split()
                if int(data[0]) > 30: 
                    if int(data[0]) == 1022:
                        pass
                    else:
                        print(data[0], "omitted")
                    continue

                if self.players[int(data[0])].team == self.players[int(data[1])].team:
                    team = True
                else: team = False
                self.players[int(data[0])].addkill(int(data[1]), team)
                self.players[int(data[1])].adddeath(int(data[0]))
                self.players[int(data[0])].weapons(int(data[2]))


    def results(self):
        
        toplist = {}
        for i in self.players:
            toplist[self.players[i].number] = self.players[i].killnumber
        a = sorted(toplist, key=toplist.get, reverse=True)
        
        maxlength = 0
        for i in a:
            if maxlength < len(self.players[i].name): maxlength = len(self.players[i].name)
        
        print("The results are ready:\n")

        print(f"Player {(maxlength - 5)*' '} Kills   Most Killed       Fav Gun                   Teamkills")
        for i in a:
            mostkilled_number = self.players[i].mostkilled()
            if mostkilled_number != -1:
                mostkilled = self.players[mostkilled_number].name
            else:
                mostkilled = "Ei tappoja"
            favgun = self.favgun_name(self.players[i].favgun())

            teamkills = self.players[i].teamkills

            space1 = (maxlength - len(self.players[i].name) + 2)*" "
            space2 = (7 - len(str(self.players[i].killnumber)))*" "
            space3 = (maxlength - len(mostkilled))*" "
            space4 = (25 - len(str(favgun)))*" "
            print(f"{self.players[i].name}{space1} {self.players[i].killnumber}{space2} {mostkilled} {space3}   {favgun}{space4} {teamkills}")

        

        

    @staticmethod
    def extract_player_data(player, data):
        player.data = data
        player.name = data[0]
        player.team = data[2]

    @staticmethod
    def favgun_name(number):
        gunlist = {
            -1: "None",
            1: "Shotgun",
            2: "Gauntlet",
            3: "Machinegun",
            4: "4",
            5: "5",
            6: "Rocket launcher",
            7: "Rocket launcher splash",
            8: "Plasma gun",
            9: "9",
            10: "Railgun",
            19: "Falling",
            20: "Suicide",
            22: "Mod_Trigger_Hurt"
        }
        return gunlist[number]