import os


class Reader:

    aggression = [];
    distribution = [];
    dead = [];
    productivity = [];
    time = [];

    def read_files(self, folderpath):
        filepaths = self.gather_files(folderpath)
        self.gather_values(filepaths)

    def gather_values(self, filepaths):
        for file in filepaths:
            aggression = -1
            distribution = ""
            dead = -1
            productivity = -1
            time = -1

            logfile = open(file, "r").readlines()
            for line in logfile:
                if "aggression" in line:
                    aggression = line.split(":")[1]
                if "distribution" in line:
                    distribution = line.split(":")[1]
                if "dead" in line:
                    dead = line.split(":")[1]
                if "productivity" in line:
                    productivity = line.split(":")[1]
                if "time" in line:
                    time = line.split(":")[1]
            # make sure our values have been assigned
            if not aggression == -1 and not productivity == -1 and not dead == -1 and not time == -1 and distribution != "":
                self.aggression.append(aggression)
                self.distribution.append(distribution)
                self.dead.append(dead)
                self.productivity.append(productivity)
                self.time.append(time)

    def gather_files(self, folderpath):
        filepaths = []
        for file in os.listdir(folderpath):
            if file.endswith(".LOG"):
                filepaths.append(os.path.join(folderpath, file))
        return filepaths

    def get_aggression(self):
        return self.aggression
