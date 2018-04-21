import subprocess


class Runner:

    def __init__(self, path, jar_path):
        self.path = path + "\\output"
        self.jar_path = jar_path

    def run_for_count(self, count):
        args = "java -jar " + self.jar_path + " write_log_file"
        for i in range(0, count):
            print("sim " + str(i))
            try:
                subprocess.Popen(subprocess.call(args, shell=True))
            except TypeError:
                print("finished sim " + str(i))



