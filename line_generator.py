from random import choice
from string import ascii_lowercase

class LineGenerator:
    def __init__(self, size: int):
        self._size = size
        self._line = "".join(choice(ascii_lowercase) for i in range(size))
    
    def generate(self, id: int):
        return "{0:011d},{1:011d},{2}\n".format(id, id, self._line)
