class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mins.append(val)
        else:
            self.stack.append(val)
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        if not self.stack:
            return
        else:
            self.stack.pop(-1)
            self.mins.pop(-1)

    def top(self) -> int:
        if not self.stack: 
            return
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return
        else:
            return self.mins[-1]
