from progress import Progress
from line_generator import LineGenerator
from pathlib import Path

class FileWriter:
    def __init__(self, file: Path, records: int, line_generator: LineGenerator):
        self._records = records
        self._record = 0
        self._file = file
        self._line_generator = line_generator
        self._buffer_size = 50000
        self._buffer = [self._buffer_size]
        self._file = file
    
    def _fill_buffer(self):
        self._buffer.clear()
        l = 0
        while l < self._buffer_size and self._record < self._records:
            self._buffer.append(self._line_generator.generate((self._record + 1) * 2))
            self._record += 1
            l += 1
        return self._buffer

    def write(self, progress: Progress):
        with open(self._file, "w") as file:
            file.write("cpf,id,data\n")
            while self._record < self._records:
                buffer = self._fill_buffer()
                file.write("".join(buffer))
                progress.next(n = len(buffer))
            progress.finish()
