import datetime
from src.Reader import Reader
from src.Writer import Writer
from src.Runner import Runner

path = "C:\\Users\\User\\Documents\\" + datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%S")

runner = Runner(path)
reader = Reader(path)
writer = Writer(path)

reader.read_files()
writer.write_file(reader.aggression, reader.distribution, reader.dead, reader.productivity, reader.time)
