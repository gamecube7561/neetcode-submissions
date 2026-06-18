class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        
    def push(self, val: int) -> None:
        if self.min is None:

            self.min = val
        else:
            self.stack.append(val-self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        popped = self.stack.pop() 
        if popped < 0:
            self.min = self.min - popped

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min
        else:
            return self.stack[-1] + self.min

    def getMin(self) -> int:
        return self.min

