
class Writer:

    def __init__(self, path):
        self.path = path + "\\data"

    def write_file(self, aggression, distribution, dead, productivity, time):
        csv = open(self.path + "swarmdata.csv", "w")
        title_row = "aggression,distribution,dead,productivity,time\n"
        csv.write(title_row)
        for index, aggression in enumerate(aggression):
            row = aggression[index] + "," + distribution[index] + "," + dead[index] + "," + productivity[index] + "," + time[index]
            row = row.replace("\n", '')
            row = row + "\n"
            csv.write(row)
