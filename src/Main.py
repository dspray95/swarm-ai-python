import datetime
from src.Reader import Reader
from src.Writer import Writer
from src.Runner import Runner

path = "C:\\Users\\User\\Documents\\" + datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%S")

runner = Runner(path, "C:\\Users\\User\\IdeaProjects\\swarm-ai-bee-behaviour\\out\\artifacts\\swarm_ai_bee_behaviour_jar\\swarm-ai-bee-behaviour.jar")
reader = Reader(path)
writer = Writer(path)

runner.run_for_count(2)
# reader.read_files()
# writer.write_file(reader.aggression, reader.distribution, reader.dead, reader.productivity, reader.time)