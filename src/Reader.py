import os


class Reader:

    aggression = [];
    casualties = [];
    productivity = [];
    dead = [];
    time = [];

    def read_files(self, folderpath):
        filepaths = self.get_files(folderpath)
        self.get_values(filepaths)

    def get_values(self, filepaths):
        for file in filepaths:
            aggression = -1
            casualties = -1
            productivity = -1
            dead = -1
            logfile = open(file, "r").readlines()
            for line in logfile:
                if "productivity" in line:
                    productivity = line.split(":")[1]
                if "casualties" in line:
                    casualties = line.split(":")[1]
                if "dead" in line:
                    dead = line.split(":")[1]
            if not aggression == -1 and not productivity == -1 and not casualties == -1 and not dead == -1: #make sure our values have been assigned
                self.productivity.append(productivity)
                self.casualties.append(casualties)
                self.aggression.append(aggression)
                self.dead.append(dead)

    def get_files(self, folderpath):
        filepaths = []
        for file in os.listdir(folderpath):
            if file.endswith(".LOG"):
                filepaths.append(os.path.join(folderpath, file))
        return filepaths
