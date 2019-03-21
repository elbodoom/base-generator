import random
from progress import Progress
from pathlib import Path

class Sampler:
    def __init__(self, file: Path, records: int, max_id: int):
        self._file = file
        self._elements = random.sample(range(1, max_id + 1), k = records)
    
    def generate(self, progress: Progress):
        with open(self._file, "w") as file:
            file.write("cpf\n")
            for e in self._elements:
                file.write("{0:011d}\n".format(e))
                progress.next()
        progress.finish()
