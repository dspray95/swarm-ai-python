import os


class Reader:

    aggression = []
    distribution = []
    dead = []
    productivity = []
    time = []

    def __init__(self, path):
        self.path = path + "\\output"

    def read_files(self):
        paths = self.gather_files()
        self.gather_values(paths)

    def gather_values(self, paths):
        for file in paths:
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

    def gather_files(self):
        paths = []
        for file in os.listdir(self.path):
            if file.endswith(".LOG"):
                paths.append(os.path.join(self.path, file))
        return paths
