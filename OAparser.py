"""
Parser handles reading and interpreting the OA logfile
"""


class Parser:
    

    def __init__(self, logfile):
        self.logfile = logfile
        self.loglist = []
        self.log = {}

        self.open()
        self.get_timecodes()
        self.get_commands()

    def open(self):
        try:
            f = open(self.logfile)
            for line in f:
                self.loglist.append(line)
        except IOError:
            print("File", self.logfile, "not found!")
    
    def get_timecodes(self):
        for i in self.loglist:
            self.log[i[0:7].strip()] = i[7:].strip()
    
    def get_commands(self):
        remove = []
        for i in self.log:
            print(self.log[i])
            try:
                a = self.log[i].split(":")
                self.log[i] = [a[0], a[1]]
            except IndexError:
                remove.append(i)
        for i in remove:
            self.log.pop(i)