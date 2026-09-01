class Deque:
    
    def __init__(self):
        self.deque = []

    def isEmpty(self) -> bool:
        return self.deque == []

    def append(self, value: int) -> None:
        self.deque.append(value)

    def appendleft(self, value: int) -> None:
        self.deque.insert(0, value)

    def pop(self) -> int:
        return self.deque.pop() if self.deque else -1

    def popleft(self) -> int:
        return self.deque.pop(0) if self.deque else -1
