from src.Reader import Reader
from src.Writer import Writer

folderpath = "C:\\Users\\User\\swarm-ai-mobbing\\log"
reader = Reader()
writer = Writer()
reader.read_files(folderpath)
writer.write_file(folderpath, reader.aggression, reader.distribution, reader.dead, reader.productivity, reader.time)