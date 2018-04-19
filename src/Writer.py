import csv


class Writer:

    def write_file(self, filepath, aggression, distribution, dead, productivity, time):
        csv = open(filepath + "swarmdata.csv", "w")
        titlerow = "aggression,distribution,dead,productivity,time\n"
        csv.write(titlerow)
        for index, aggression in enumerate(aggression):
            row = aggression[index] + "," + distribution[index] + "," + dead[index] + "," + productivity[index] + "," + time[index]
            csv.write(row)
