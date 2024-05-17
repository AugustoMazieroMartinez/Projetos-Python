from typing import Optional
class Node:
    def __init__(self, dado: int):
        self.value = dado
        self.next = Optional['Node'] = None
        self.prev = Optional['Node'] = None